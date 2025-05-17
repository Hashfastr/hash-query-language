curl -Lo "./antlr4/antlr.jar" "https://github.com/rrevenantt/antlr4rust/releases/download/antlr4-4.8-2-Rust0.3.0-beta/antlr4-4.8-2-SNAPSHOT-complete.jar"

export CLASSPATH="$PWD/antlr/antlr.jar:$CLASSPATH"
# simplify the use of the tool to generate lexer and parser
alias antlr4="java -Xmx500M -cp '$PWD/antlr4/antlr.jar:$CLASSPATH' org.antlr.v4.Tool"
# simplify the use of the tool to test the generated code
alias grun="java -Xmx500M -cp '$PWD/antlr4/antlr.jar:$CLASSPATH' org.antlr.v4.gui.TestRig"

cat << EOF

Done!

You can now run

antlr4 -Dlanguage=Rust -visitor Hql.g4
EOF