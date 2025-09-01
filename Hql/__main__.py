import sys    

from Hql.Parser import Parser, SigmaParser
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Exceptions import HacExceptions as hace
from Hql.Compiler import Compiler, HqlCompiler
from Hql.Query import Query
from Hql.Hac import Parser as HaCParser
from Hql.Config import Config

import json
import logging
import argparse, sys
import cProfile, pstats, time
from pathlib import Path

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
    file_ops = parser.add_mutually_exclusive_group(required=True)
    file_ops.add_argument('-f', '--file', help="Hql/Sigma file")
    file_ops.add_argument('-d', '--directory', help="File to compile")
    parser.add_argument('-o', '--output', help='Output dir otherwise stdout')
    parser.add_argument('-v', '--verbose', help="Set verbosity to debug", action='store_true')
    parser.add_argument('-l' '--logging-level', help="Verbosity level 1-5, where 5 is debug, 1 is critical, default is 3, warning.", type=int)
    parser.add_argument('-p', '--profile', help="Profile the performance of Hql", action='store_true')
    parser.add_argument('-c', '--config', help="Location of the config file")
    parser.add_argument('-nx', '--no-exec', help="Only compile, don't execute", action='store_true')
    parser.add_argument('-dpar', '--deparse', help="Deparse the program before compiling", action='store_true')
    parser.add_argument('-dec', '--decompile', help="Decompile the program before running", action='store_true')
    parser.add_argument('-hac', '--render-hac', help="Renders HaC to a given format (md, json)")
    parser.add_argument('-sig', '--sigma', help="Input file is a Sigma file", action='store_true')
    parser.add_argument('-om', '--omni', help="Process both Sigma and Hql if given the input", action='store_true')
    
    args = parser.parse_args()
    
    profiler = None
    if args.profile:
        profiler = cProfile.Profile()
        profiler.enable()
    
    if args.l__logging_level:
        config_logging(args.l__logging_level)
    elif args.verbose:
        config_logging(5)
        
    if args.config == None:
        conf_path = "./conf"
    else:
        conf_path = args.config
    conf = Config(Path(conf_path))
        
    sigma_files:list[Path] = []
    hql_files:list[Path] = []

    if args.directory:
        path = Path(args.directory)

        # Hql
        for file in path.rglob('*.hql'):
            if file.is_file():
                hql_files.append(file)

        # yml
        for file in path.rglob('*.yml'):
            if file.is_file():
                sigma_files.append(file)

    else:
        if args.sigma:
            sigma_files.append(Path(args.file))
        else:
            hql_files.append(Path(args.file))

    errors = []
    successes = []

    if args.sigma or args.omni:
        for i in sigma_files:
            with i.open(mode='r') as f:
                txt = f.read()

            try:
                print(run_query(txt, args, i, conf))
            except Exception as e:
                logging.critical('Exception caught when running query')
                logging.critical(e)
                errors.append(i)
                continue

            successes.append(i)
    
    if not args.sigma or args.omni:
        for i in hql_files:
            with i.open(mode='r') as f:
                txt = f.read()

            try:
                print(run_query(txt, args, i, conf))
            except Exception as e:
                logging.exception('Exception caught when running query')
                # logging.critical(e.__traceback__)
                errors.append(i)
                continue

            successes.append(i)

    logging.info(f'Finished execution {len(errors)} errors, {len(successes)} successes')
    
    #####################
    ## Profiling stuff ##
    #####################
    
    if args.profile:
        assert profiler
        profiler.disable()
        
        with open('./profile.txt', mode='w+') as f:
            stats = pstats.Stats(profiler, stream=f)
            stats.sort_stats('time')
            stats.print_stats()
            
        logging.info("Performance metrics outputted to profile.txt")

    if errors:
        return -1
        
def run_query(text:str, args, src:Path, conf:Config) -> str:
    from Hql.Context import Context
    from Hql.Data import Data

    ##################################
    ## Generate HaC (if applicable) ##
    ##################################

    logging.debug(f'Parsing HaC for {src.as_posix()}...')
    if args.sigma:
        parser = SigmaParser(text)
        hac = parser.gen_hac()

    else:
        try:
            parser = HaCParser.Parser(text=text)
            hac = parser.assemble()
        except hace.LexerException:
            hac = None

    if args.render_hac:
        if not hac:
            logging.critical('Hql file does not contain a valid HaC comment!')
            return ''

        return hac.render(args.render_hac)

    #######################
    ## Generate Assembly ##
    #######################
    
    logging.debug(f'Parsing {src.as_posix()}...')
    start = time.perf_counter()

    if args.sigma or args.omni:
        parser = SigmaParser(text)
    else:
        parser = Parser(text)
    parser.assemble()
    
    logging.debug('Done.')
    
    end = time.perf_counter()
    logging.debug(f'Parsing took {end - start}')
    
    if args.asm_show:
        # Use print to give a raw output
        return str(parser.assembly)

    if args.deparse:
        deparse = ''

        if hac:
            deparse += hac.render(target='decompile')
            deparse += '\n'

        if not isinstance(parser.assembly, Query):
            raise hqle.CompilerException(f'Attempting to compile non-Query assembly {type(parser.assembly)}')

        deparse += parser.assembly.decompile(Context(Data()))
        return deparse
        
    ######################
    ## Compile Assembly ##
    ######################
    
    logging.debug("Compiling...")
    start = time.perf_counter()

    if not isinstance(parser.assembly, Query):
        raise hqle.CompilerException(f'Attempting to compile non-Query assembly {type(parser.assembly)}')
    
    compiler = HqlCompiler(conf, parser.assembly)
    
    end = time.perf_counter()
    logging.debug("Done.")
    
    logging.debug(f"Compiling took {end - start}")

    if args.decompile:
        return compiler.decompile()
   
    if args.no_exec:
        return ''
    
    #############
    ## Queries ##
    #############

    logging.debug("Running")
    start = time.perf_counter()
    
    results = compiler.run().data
   
    end = time.perf_counter() 
    logging.debug("Ran")
    logging.debug(f"Computation took {end - start}")
    
    logging.debug(f'Got {len(results)} results from query')
    
    return json.dumps(results.to_dict(), default=repr)
    
if __name__ == "__main__":
    main()
