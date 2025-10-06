#!/bin/bash
shopt -s expand_aliases
. ./setup-antlr4.sh
antlr4 PCRELexer.g4 -o .
antlr4 -lib . PCREParser.g4 -o .
antlr4 -Dlanguage=Python3 -visitor -lib . PCREParser.g4
