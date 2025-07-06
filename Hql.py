from HqlCompiler.HqlParser import Parser
from HqlCompiler.Exceptions import *
from HqlCompiler import Compiler
import HaCEngine.Parser as HaCParser
import HaCEngine.Exceptions as HacExceptions


import json
import logging
import argparse, sys
import cProfile, pstats, time

def config_logging(level:int):
    logging.basicConfig(
        stream=sys.stderr,
        format="%(levelname)s - %(filename)s:%(lineno)d - %(message)s"
    )
    
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
    parser.add_argument('-c', '--config', help="Location of the config file")
    parser.add_argument('-nx', '--no-exec', help="Only compile, don't execute", action='store_true')
    parser.add_argument('-hac', '--render-hac', help="Renders HaC to a given format (md, json)")
    
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
        
    if args.config == None:
        conf_file = "./conf.json"
    else:
        conf_file = args.config
        
    ##################################
    ## Generate HaC (if applicable) ##
    ##################################
    if args.render_hac:
        try:
            parser = HaCParser.Parser(filename=args.file)
        except HacExceptions.LexerException:
            logging.critical('hql file does not contain a valid HaC comment!')
            return -1

        hac = parser.assemble()
        print(hac.render(args.render_hac))
        return

    #######################
    ## Generate Assembly ##
    #######################
    
    logging.debug('Parsing...')
    start = time.perf_counter()

    try:
        parser = Parser(args.file)
        parser.assemble()
    except HqlException as e:
        logging.critical('Exception caught when assembling')
        logging.critical(e)
        return -1
    
    if args.asm_show:
        # Use print to give a raw output
        print(parser.assembly)
        return
        
    logging.debug('Done.')
    
    end = time.perf_counter()
    logging.debug(f'Parsing took {end - start}')
        
    ######################
    ## Compile Assembly ##
    ######################
    
    # with open(rule_file, mode="r") as f:
    #     ruleset = json.loads(f.read())
    
    logging.debug("Compiling...")
    start = time.perf_counter()
    
    compiler = Compiler(conf_file, parser.assembly)
    compiler.compile()
    
    end = time.perf_counter()
    logging.debug("Done.")
    
    logging.debug(f"Compiling took {end - start}")
   
    if args.no_exec:
        return
    
    #############
    ## Queries ##
    #############

    logging.debug("Running")
    start = time.perf_counter()
    
    results = compiler.run()
    print(json.dumps(results.to_dict(), default=repr))
   
    end = time.perf_counter() 
    logging.debug("Ran")
    logging.debug(f"Computation took {end - start}")
    
    logging.debug(f'Got {len(results)} results from query')

    #####################
    ## Profiling stuff ##
    #####################
    
    if args.profile:
        profiler.disable()
        
        with open('./profile.txt', mode='w+') as f:
            stats = pstats.Stats(profiler, stream=f)
            stats.sort_stats('time')
            stats.print_stats()
            
        print("Performance metrics outputted to profile.txt")
        
if __name__ == "__main__":
    main()
