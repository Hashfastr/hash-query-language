use log;
// use fern::colors::{Color, ColoredLevelConfig};

use std::time::{SystemTime, Instant};

use std::fs;
use std::error::Error;

mod argparser;
use argparser::parse_args;

mod parser;
mod grammar;

fn setup_logger(debug:bool) -> Result<(), fern::InitError> {
    let ll:log::LevelFilter = if debug {
        log::LevelFilter::Debug
    } else {
        log::LevelFilter::Info
    };

    fern::Dispatch::new()
        .format(|out, message, record| {
            out.finish(format_args!(
                "[{} {} {}] {}",
                humantime::format_rfc3339_seconds(SystemTime::now()),
                record.level(),
                record.target(),
                message
            ))
        })
        .level(ll)
        .chain(std::io::stdout())
        .chain(fern::log_file("output.log")?)
        .apply()?;

    Ok(())
}

fn main() -> Result<(), Box<dyn Error>> {
    let cmd = parse_args()?;
    let cmd_name = cmd.subcommand_name().unwrap();
    let matches = cmd.subcommand_matches(cmd_name).unwrap();

    setup_logger(*matches.get_one::<bool>("verbose").unwrap())?;

    let queryfile = matches
        .get_one::<String>("file")
        .map(String::as_str).unwrap();

    /*
     * Parse out and generate assembly
     */
    log::debug!("Parsing...");
    let start = Instant::now();

    parser::assemble(queryfile);

    let elapsed = start.elapsed();
    log::debug!("Parsing took {:?}", elapsed);

    /*
     * Compile Assembly
     */

    /*
     * Query
     */

    Ok(())
}
