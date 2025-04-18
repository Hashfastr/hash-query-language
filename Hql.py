from antlr4 import *
from grammar.HqlLexer import HqlLexer
from grammar.HqlParser import HqlParser
from HqlVisitor import Visitor
import sys
import logging
import argparse

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
        raise(f'Invalid verbosity {level}')

def get_token_name(type:int) -> str:
    return HqlLexer.symbolicNames[type]

def parse_file(filename:str) -> CommonTokenStream:
    try:
        with open(filename, 'r') as f:
            input_text = f.read()
            lexer = HqlLexer(InputStream(input_text))
            token_stream = CommonTokenStream(lexer)
            parser = HqlParser(token_stream)
    except Exception as e:
        logging.error(f"Failed to open file {filename}")
        logging.error(str(e))
    
    tree = parser.query()
    
    return tree

def main():
    parser = argparse.ArgumentParser(prog=sys.argv[0])
    parser.add_argument('-s', '--show', help='Show the json of the parsed data and exit', action='store_true')
    parser.add_argument('-f', '--file', help="File to compile")
    parser.add_argument('-v', '--verbose', help="Set verbosity to debug", action='store_true')
    parser.add_argument('-l' '--logging-level', help="Verbosity level 1-5, where 5 is debug, 1 is critical, default is 3, warning.", type=int)
    
    args = parser.parse_args()
    
    if args.l__logging_level:
        config_logging(args.l__logging_level)
    elif args.verbose:
        config_logging(5)
        
    tree = parse_file(args.file)

    visitor = Visitor()
    result = visitor.visit(tree)

    if args.show:
        # Use print to give a raw output
        print(result)
        return
    else:
        logging.debug(result)

if __name__ == "__main__":
    main()