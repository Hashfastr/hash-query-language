use log;
use std::fs;
use std::error::Error;

use super::grammar::hqllexer::HqlLexer;
use super::grammar::hqlvisitor::HqlVisitor;
use super::grammar::hqlparser::*;

use antlr_rust::common_token_stream::CommonTokenStream;
use antlr_rust::input_stream::InputStream;
use antlr_rust::parser_rule_context::ParserRuleContext;
use antlr_rust::tree::{ErrorNode, ParseTreeListener, TerminalNode};

pub trait Visitor<'input>: HqlVisitor<'input> {
    /**
	 * Visit a parse tree produced by {@link HqlParser#query}.
	 * @param ctx the parse tree
	 */
	fn visit_query(&mut self, ctx: &QueryContext<'input>) {
        self.visit_children(ctx)
    }
}

pub fn assemble(queryfile:&str) -> Result<(), Box<dyn Error>> {
    let query_text = fs::read_to_string(queryfile)?;
    let static_query: &'static str = Box::leak(query_text.into_boxed_str());

    let lexer = HqlLexer::new(InputStream::new(static_query));
    let mut parser = HqlParser::new(CommonTokenStream::new(lexer));
    let tree = parser.query()?;

    // let output = tree.

    Ok(())
}