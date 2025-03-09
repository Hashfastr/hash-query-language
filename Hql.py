from antlr4 import *
from grammar.HqlLexer import HqlLexer
from grammar.HqlParser import HqlParser
from HqlVisitor import Visitor
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

    visitor = Visitor()
    result = visitor.visit(tree)
    
    print(result)

if __name__ == "__main__":
    main()