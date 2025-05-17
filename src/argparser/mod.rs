use std::error::Error;
use log::{info};

use clap::builder::{ValueParser, ValueParserFactory};
use clap::{ArgAction, Arg, Parser, Subcommand};

pub fn parse_args() -> Result<clap::ArgMatches, Box<dyn Error>> {
    let cmd = clap::Command::new("Hql")
        .bin_name("Hql")
        // .styles(CLAP_STYLING)
        .subcommand_required(true)
        .subcommand(
            clap::command!("asm").arg(
                Arg::new("file")
                .short('f')
                .long("file")
                .required(true)
                .action(ArgAction::Set)
                .value_name("HQLFILE")
                .help("The query file to input")
            )
            .arg(
                Arg::new("verbose")
                .short('v')
                .long("verbose")
                .global(true)
                .action(ArgAction::SetTrue)
                .help("Enable verbose output")
            )
        );

    let matches = cmd.get_matches();

    Ok(matches)
}

// // See also `clap::style::CLAP_STYLING`
// pub const CLAP_STYLING: clap::builder::styling::Styles = clap::builder::styling::Styles::styled()
//     .header(clap::style::HEADER)
//     .usage(clap::style::USAGE)
//     .literal(clap::style::LITERAL)
//     .placeholder(clap::style::PLACEHOLDER)
//     .error(clap::style::ERROR)
//     .valid(clap::style::VALID)
//     .invalid(clap::style::INVALID);