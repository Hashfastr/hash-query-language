from Hql.Types.Hql import HqlTypes as hqlt
from Hql.Types.Compiler import CompilerType
import logging
from typing import Union

from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import register_type, get_type
# from ..Types.Compiler import CompilerType

class ESTypes():
    class ESType(CompilerType):
        def __init__(self, base:type, inner:Union[None, type]=None):
            CompilerType.__init__(self, base, inner=inner)
    
    @staticmethod
    def from_name(name:str):
        return get_type(f'elasticsearch_{name}')
            
    @register_type('elasticsearch_text')
    @register_type('elasticsearch_match_only_text')
    class text(ESType):
        def __init__(self):
            ESTypes.ESType.__init__(self, hqlt.string)

    @register_type('elasticsearch_boolean')
    class boolean(ESType):
        def __init__(self):
            ESTypes.ESType.__init__(self, hqlt.bool)

    @register_type('elasticsearch_scaled_float')
    class scaled_float(ESType):
        def __init__(self):
            ESTypes.ESType.__init__(self, hqlt.decimal)

    @register_type('elasticsearch_half_float')
    class half_float(ESType):
        def __init__(self):
            ESTypes.ESType.__init__(self, hqlt.float)
    
    @register_type('elasticsearch_float')
    class float(ESType):
        def __init__(self):
            ESTypes.ESType.__init__(self, hqlt.float)
        
    @register_type('elasticsearch_double')
    class double(ESType):
        def __init__(self):
            ESTypes.ESType.__init__(self, hqlt.double)
    
    @register_type('elasticsearch_byte') 
    class byte(ESType):
        def __init__(self):
            ESTypes.ESType.__init__(self, hqlt.byte)
    
    @register_type('elasticsearch_short') 
    class short(ESType):
        def __init__(self):
            ESTypes.ESType.__init__(self, hqlt.short)
    
    @register_type('elasticsearch_integer') 
    class integer(ESType):
        def __init__(self):
            ESTypes.ESType.__init__(self, hqlt.int)
    
    @register_type('elasticsearch_long') 
    class long(ESType):
        def __init__(self):
            ESTypes.ESType.__init__(self, hqlt.long)
    
    @register_type('elasticsearch_unsigned_long') 
    class unsigned_long(ESType):
        def __init__(self):
            ESTypes.ESType.__init__(self, hqlt.ulong)
    
    @register_type('elasticsearch_ip') 
    class ip(ESType):
        def __init__(self):
            ESTypes.ESType.__init__(self, hqlt.string)
        
    @register_type('elasticsearch_date')
    class date(ESType):
        def __init__(self):
            ESTypes.ESType.__init__(self, hqlt.datetime)
    
    @register_type('elasticsearch_date_nanos') 
    class date_nanos(ESType):
        def __init__(self):
            ESTypes.ESType.__init__(self, hqlt.datetime)
        
    @register_type('elasticsearch_date_range')
    class date_range(ESType):
        def __init__(self):
            ESTypes.ESType.__init__(self, hqlt.range, inner=hqlt.datetime)
    
    @register_type('elasticsearch_integer_range') 
    class integer_range(ESType):
        def __init__(self):
            ESTypes.ESType.__init__(self, hqlt.range, inner=hqlt.int)

    @register_type('elasticsearch_float_range')
    class float_range(ESType):
        def __init__(self):
            ESTypes.ESType.__init__(self, hqlt.range, inner=hqlt.float)
        
    @register_type('elasticsearch_long_range')   
    class long_range(ESType):
        def __init__(self):
            ESTypes.ESType.__init__(self, hqlt.range, inner=hqlt.long)
        
    @register_type('elasticsearch_double_range') 
    class double_range(ESType):
        def __init__(self):
            ESTypes.ESType.__init__(self, hqlt.range, inner=hqlt.double)

    @register_type('elasticsearch_ip_range') 
    class ip_range(ESType):
        def __init__(self):
            # Might need to specify the type of ip
            ESTypes.ESType.__init__(self, hqlt.range, inner=hqlt.ip)
    
    @register_type('elasticsearch_keyword') 
    class keyword(ESType):
        def __init__(self):
            ESTypes.ESType.__init__(self, hqlt.string)
    
    @register_type('elasticsearch_constant_keyword') 
    class constant_keyword(ESType):
        def __init__(self):
            ESTypes.ESType.__init__(self, hqlt.string)
    
    @register_type('elasticsearch_wildcard') 
    class wildcard(ESType):
        def __init__(self):
            ESTypes.ESType.__init__(self, hqlt.string)
    
    @register_type('elasticsearch_binary') 
    class binary(ESType):
        def __init__(self):
            ESTypes.ESType.__init__(self, hqlt.string)
    
    @register_type('elasticsearch_object') 
    class object(ESType):
        def __init__(self):
            ESTypes.ESType.__init__(self, hqlt.object)
    
    @register_type('elasticsearch_flattened') 
    class flattened(ESType):
        def __init__(self):
            ESTypes.ESType.__init__(self, hqlt.object)
        
    @register_type('elasticsearch_nested')
    class nested(ESType):
        def __init__(self):
            ESTypes.ESType.__init__(self, hqlt.object)
    
    @register_type('elasticsearch_alias') 
    class alias(ESType):
        def __init__(self):
            logging.warning("Elasticsearch type 'alias' not implemented at the moment")
            logging.warning("This is a metatype, I don't have examples")
            ESTypes.ESType.__init__(self, hqlt.string)
        
    @register_type('elasticsearch_point')
    class point(ESType):
        def __init__(self):
            ESTypes.ESType.__init__(self, hqlt.multivalue, inner=hqlt.double)
        
    @register_type('elasticsearch_geo_point')
    class geo_point(ESType):
        def __init__(self):
            ESTypes.ESType.__init__(self, hqlt.multivalue, inner=hqlt.double)
    
    @register_type('elasticsearch_shape') 
    class shape(ESType):
        def __init__(self):
            ESTypes.ESType.__init__(self, hqlt.multivalue, inner=hqlt.double)
                    
    @register_type('elasticsearch_geo_shape')   
    class geo_shape(ESType):
        def __init__(self):
            ESTypes.ESType.__init__(self, hqlt.multivalue, inner=hqlt.double)
