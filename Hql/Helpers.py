from pathlib import Path
from Hql.Config import Config
from Hql.Data import Data
import logging, time
from typing import Union

def run_query(text:str, conf:Config, src:Union[str, Path]='', **kwargs) -> Union[Data, str]:
    from Hql.Exceptions import HqlExceptions as hqle
    from Hql.Exceptions import HacExceptions as hace
    from Hql.Context import Context
    from Hql.Data import Data
    from Hql.Parser import Parser, SigmaParser
    from Hql.Compiler import HqlCompiler
    from Hql.Hac import Parser as HaCParser
    from Hql.Query import Query

    ##################################
    ## Generate HaC (if applicable) ##
    ##################################

    if isinstance(src, Path):
        src = src.as_posix()

    logging.debug(f'Parsing HaC for {src}...')
    if kwargs.get('sigma', False):
        parser = SigmaParser(text)
        hac = parser.gen_hac()

    else:
        try:
            hac = HaCParser.parse_text(text, str(src))
        except hace.LexerException:
            hac = None

    if kwargs.get('render_hac', ''):
        if not hac:
            logging.critical('Hql file does not contain a valid HaC comment!')
            return ''

        return hac.render(kwargs['render_hac'])

    #######################
    ## Generate Assembly ##
    #######################
    
    logging.debug(f'Parsing {src}...')
    start = time.perf_counter()

    if kwargs.get('sigma', False) or kwargs.get('omni', False):
        parser = SigmaParser(text)
    else:
        parser = Parser(text)
    parser.assemble()
    
    logging.debug('Done.')
    
    end = time.perf_counter()
    logging.debug(f'Parsing took {end - start}')
    
    if kwargs.get('asm_show', False):
        # Use print to give a raw output
        return str(parser.assembly)

    if kwargs.get('deparse', False):
        deparse = ''

        if hac:
            deparse += hac.render(target='decompile')
            deparse += '\n'

        if not isinstance(parser.assembly, Query):
            raise hqle.CompilerException(f'Attempting to compile non-Query assembly {type(parser.assembly)}')

        deparse += parser.assembly.decompile(Context(Data()))
        return deparse
        
    ######################
    ## Compile Assembly ##
    ######################
    
    logging.debug("Compiling...")
    start = time.perf_counter()

    if not isinstance(parser.assembly, Query):
        raise hqle.CompilerException(f'Attempting to compile non-Query assembly {type(parser.assembly)}')
    
    compiler = HqlCompiler(conf, parser.assembly)
    
    end = time.perf_counter()
    logging.debug("Done.")
    
    logging.debug(f"Compiling took {end - start}")

    if kwargs.get('plan', False):
        assert compiler.root
        return compiler.root.render()

    # if kwargs.get('decompile:
    #     return compiler.decompile()
   
    if kwargs.get('no_exec', False):
        return ''
    
    #############
    ## Queries ##
    #############

    logging.debug("Running")
    start = time.perf_counter()
    
    results = compiler.run().data
   
    end = time.perf_counter() 
    logging.debug("Ran")
    logging.debug(f"Computation took {end - start}")
    
    logging.debug(f'Got {len(results)} results from query')
    
    return results
