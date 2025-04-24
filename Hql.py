from antlr4 import *
from compiler.grammar.HqlLexer import HqlLexer
from compiler.grammar.HqlParser import HqlParser
from compiler.HqlVisitor import Visitor
import sys
import json
import logging
import argparse
from compiler.Compiler import Compiler
import shutil
import cProfile, pstats
import time
import subprocess

def config_logging(level:str):
    logging.basicConfig()
    
    if level == 5:
        logging.getLogger().setLevel(logging.DEBUG)
    elif level == 4:
        logging.getLogger().setLevel(logging.INFO)
    elif level == 3:
        logging.getLogger().setLevel(logging.WARNING)
    elif level == 2:
        logging.getLogger().setLevel(logging.ERROR)    
    elif level == 1:
        logging.getLogger().setLevel(logging.CRITICAL)
    else:
        logging.error(f"Invalid verbosity level {level}")
        logging.error(f"Default is WARNING (3), but I'm exiting...")
        raise Exception(f'Invalid verbosity {level}')

def get_token_name(type:int) -> str:
    return HqlLexer.symbolicNames[type]

def parse_file(filename:str) -> CommonTokenStream:
    start = time.perf_counter()
    
    try:
        with open(filename, 'r') as f:
            input_text = f.read()
            lexer = HqlLexer(InputStream(input_text))
            token_stream = CommonTokenStream(lexer)
            parser = HqlParser(token_stream)
    except Exception as e:
        logging.error(f"Failed to open file {filename}")
        logging.error(str(e))
        raise e
    
    tree = parser.query()
    
    end = time.perf_counter()
    logging.debug(f'Parsing took {end - start}s')
    
    return tree

def main():
    parser = argparse.ArgumentParser(prog=sys.argv[0])
    parser.add_argument('-asm', '--asm-show', help='Show the json of the parsed data and exit', action='store_true')
    parser.add_argument('-f', '--file', help="File to compile", required=True)
    parser.add_argument('-v', '--verbose', help="Set verbosity to debug", action='store_true')
    parser.add_argument('-l' '--logging-level', help="Verbosity level 1-5, where 5 is debug, 1 is critical, default is 3, warning.", type=int)
    parser.add_argument('-r', '--rule-set', help="The ruleset used for compiling, defaults to ./rules.json")
    parser.add_argument('-nc', '--no-clean', help="Should Hql not clean up container files after execution?", action='store_true')
    parser.add_argument('-p', '--profile', help="Profile the performance of Hql", action='store_true')
    parser.add_argument('-co', '--compose-override', help="Override the compose binary found in the path")
    
    args = parser.parse_args()
    
    if args.profile:
        profiler = cProfile.Profile()
        profiler.enable()
    
    if args.l__logging_level:
        config_logging(args.l__logging_level)
    elif args.verbose:
        config_logging(5)
    
    # unused for now
    if args.rule_set == None:
        rule_file = "./rules.json"
    else:
        rule_file = args.rule_set

    #######################
    ## Generate Assembly ##
    #######################
    
    logging.debug('Parsing...')
    
    try:
        tree = parse_file(args.file)
    except:
        return -1

    visitor = Visitor()
    result = visitor.visit(tree)
    
    if result == None:
        logging.error("Compiler error!")
        logging.error("Parser returned None instead of valid assembly")
        logging.error("Import error?")
        return -1
    
    if args.asm_show:
        # Use print to give a raw output
        print(result)
        return
        
    logging.debug('Done.')
        
    ######################
    ## Compile Assembly ##
    ######################
    
    # with open(rule_file, mode="r") as f:
    #     ruleset = json.loads(f.read())
    
    logging.debug("Compiling...")
    
    compiler = Compiler('./conf.json', result.to_dict())
    compiler.compile()
    compiler.gen_commands()
    compiler.write_to_disk()
        
    logging.debug("Done.")
    
    ####################
    ## Run Containers ##
    ####################
    
    logging.debug('Running entry commands')
    
    for cmd in compiler.cmds['entry']:
        subprocess.run(
            cmd,
            cwd=compiler.working_dir(),
            check=True,
            capture_output=True
        )
    
    logging.debug('Capturing')
    
    subprocess.run(
        compiler.cmds['capture'],
        cwd=compiler.working_dir(),
        check=True,
        capture_output=True
    )
    
    logging.debug('Running exit commands')
    
    for cmd in compiler.cmds['exit']:
        subprocess.run(
            cmd,
            cwd=compiler.working_dir(),
            check=True,
            capture_output=True
        )
        
    logging.debug('Cleaning files')

    if not args.no_clean:
        shutil.rmtree(compiler.working_dir())
    
    if args.profile:
        profiler.disable()
        
        with open('./profile.txt', mode='w+') as f:
            stats = pstats.Stats(profiler, stream=f)
            stats.sort_stats('time')
            stats.print_stats()
            
        print("Performance metrics outputted to profile.txt")
        
if __name__ == "__main__":
    main()