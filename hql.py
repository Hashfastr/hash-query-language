from antlr4 import *
from grammar.HqlLexer import HqlLexer
from grammar.HqlParser import HqlParser
from grammar.HqlListener import HqlListener
import sys


with open('tests/ssh-users.txt', 'r') as f:
  input_text = f.read()
  lexer = HqlLexer(InputStream(input_text))
  stream = CommonTokenStream(lexer)
  parser = HqlParser(stream)

  tree = parser.query()

  print(tree.toStringTree(recog=parser))