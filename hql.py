from antlr4 import *
from grammar.HqlLexer import HqlLexer
from grammar.HqlParser import HqlParser
from HqlListener import HqlListener
import sys

def get_token_name(type:int) -> str:
    return HqlLexer.symbolicNames[type]

def parse_file(filename:str) -> CommonTokenStream:
    with open(filename, 'r') as f:
        input_text = f.read()
        lexer = HqlLexer(InputStream(input_text))
        token_stream = CommonTokenStream(lexer)
        parser = HqlParser(token_stream)
    
    tree = parser.query()
    
    #print(tree.toStringTree(recog=parser))

    return tree

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} [filename]")
        return
    
    tree = parse_file(sys.argv[1])

    walker = ParseTreeWalker()
    listener = HqlListener()
    
    listener.statements = {}
    walker.walk(listener, tree)

if __name__ == "__main__":
    main()