# Hac Grammar
No need to recompile, this dir contains the compiled base files.
Just need the Lexer, Parser, and Visitor python files, the two g4 files, 
Hac.g4 and HacTokens.g4 are all that's needed to compile those files.
Recompiling should not modify anything as if modifications are needed to these
files then they are just made in a subclass file inheiriting the original.

## Recompiling
```
# you need java
source ./setup-antlr4.sh

# Generates the python files needed
antlr4 -Dlanguage=Python3 -visitor ./Hac.g4
```

This will generate some other files that I've ignored that are not needed.

```
Hac.interp
Hac.tokens
HacLexer.interp
HacLexer.tokens
HacListener.py
```

We use the Visitor not the Listener so it's ignored and removed from this repo.
Additionally, the setup will put a copy of antlr4 in the antlr4 directory.
It is ignored as we should not be the ones distributing that jar file.

## Changing antlr4 versions
Edit the setup file to reflect it.

```
VERSION="4.13.2"
```

Then recompile.

## Debug
### Generating graphs using grun
Where previously we compiled antlr to python, we need to compile it to java for grun.
Make sure you already setup antlr4 using the setup script as seen in the previous section.

```
# this generates *a lot* of java and class files
cd grammar
antlr4 -Dlanguage=Java -visitor Hac.g4
javac -cp ./antlr4/antlr-*-complete.jar Hac*.java

# runs until you kill / Ctrl-C / close the window
grun Hac top ../tests/simple.txt -gui

# Clean up via
rm *.java *.class
```
