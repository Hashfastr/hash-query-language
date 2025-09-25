import sys    

from Hql.Config import Config
from Hql import run_query
from Hql.Data import Data

import json
import logging
import argparse, sys
import cProfile, pstats
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
    # parser.add_argument('-dec', '--decompile', help="Decompile the program before running", action='store_true')
    parser.add_argument('-pl', '--plan', help="Prints the plan for the execution", action='store_true')
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

            # try:
            data = run_query(txt, conf, src=i, **vars(args))
            if isinstance(data, Data):
                print(json.dumps(data.to_dict(), default=repr))
            else:
                print(data)
            # except Exception as e:
            #     logging.critical('Exception caught when running query')
            #     logging.critical(e)
            #     errors.append(i)
            #     continue

            successes.append(i)
    
    if not args.sigma or args.omni:
        for i in hql_files:
            with i.open(mode='r') as f:
                txt = f.read()

            try:
                data = run_query(txt, conf, src=i, **vars(args))
                if isinstance(data, Data):
                    print(json.dumps(data.to_dict(), default=repr))
                else:
                    print(data)
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
        
if __name__ == "__main__":
    main()
