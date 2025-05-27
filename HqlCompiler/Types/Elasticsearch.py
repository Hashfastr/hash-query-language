from HqlCompiler.Types.Hql import HqlTypes as Hql
import logging

from HqlCompiler.Exceptions import *
from HqlCompiler.Context import register_type, get_type
# from HqlCompiler.Types.Compiler import CompilerType

class ESTypes():
    class ESType():
        def __init__(self):
            if len(type(self).__bases__):
                super().__init__()
                self.HqlType = type(self).__bases__[-1]
            else:
                self.HqlType = None
        
        def hql_schema(self):
            return self.HqlType
        
    def from_name(name:str):
        return get_type(f'elasticsearch_{name}')
            
    @register_type('elasticsearch_scaled_float')
    class scaled_float(ESType, Hql.decimal):
        ...

    @register_type('elasticsearch_half_float')
    class half_float(ESType, Hql.float):
        ...
    
    @register_type('elasticsearch_float') 
    class float(ESType, Hql.float):
        ...
        
    @register_type('elasticsearch_double')
    class double(ESType, Hql.double):
        ...
    
    @register_type('elasticsearch_byte') 
    class byte(ESType, Hql.byte):
        ...
    
    @register_type('elasticsearch_short') 
    class short(ESType, Hql.short):
        ...
    
    @register_type('elasticsearch_integer') 
    class integer(ESType, Hql.int):
        ...
    
    @register_type('elasticsearch_long') 
    class long(ESType, Hql.long):
        ...
    
    @register_type('elasticsearch_unsigned_long') 
    class unsigned_long(ESType, Hql.ulong):
        ...
    
    @register_type('elasticsearch_ip') 
    class ip(ESType, Hql.string):
        ...
        
    @register_type('elasticsearch_date')
    class date(ESType, Hql.datetime):
        ...
    
    @register_type('elasticsearch_date_nanos') 
    class date_nanos(ESType, Hql.datetime):
        ...
        
    @register_type('elasticsearch_date_range')
    class date_range(ESType, Hql.range):
        def __init__(self):
            ESTypes.ESType.__init__(self)
            Hql.range.__init__(self, Hql.datetime)
    
    @register_type('elasticsearch_integer_range') 
    class integer_range(ESType, Hql.range):
        def __init__(self):
            ESTypes.ESType.__init__(self)
            Hql.range.__init__(self, Hql.datetime)

    @register_type('elasticsearch_float_range')
    class float_range(ESType, Hql.range):
        def __init__(self):
            ESTypes.ESType.__init__(self)
            Hql.range.__init__(self, Hql.datetime)
        
    @register_type('elasticsearch_long_range')   
    class long_range(ESType, Hql.range):
        def __init__(self):
            ESTypes.ESType.__init__(self)
            Hql.range.__init__(self, Hql.datetime)
        
    @register_type('elasticsearch_double_range') 
    class double_range(ESType, Hql.range):
        def __init__(self):
            ESTypes.ESType.__init__(self)
            Hql.range.__init__(self, Hql.datetime)

    @register_type('elasticsearch_ip_range') 
    class ip_range(ESType, Hql.range):
        def __init__(self, ip_type:int):
            ESTypes.ESType.__init__(self)
            
            if ip_type not in (4, 6):
                raise CompilerException(f"Invalid IP version type {ip_type} passed to Elasticsearch type")
            
            if ip_type == 4:
                Hql.range.__init__(self, type=Hql.ip4)
            else:
                Hql.range.__init__(self, type=Hql.ip6)
    
    @register_type('elasticsearch_keyword') 
    class keyword(ESType, Hql.string):
        ...
    
    @register_type('elasticsearch_constant_keyword') 
    class constant_keyword(ESType, Hql.string):
        ...
    
    @register_type('elasticsearch_wildcard') 
    class wildcard(ESType, Hql.string):
        ...
    
    @register_type('elasticsearch_binary') 
    class binary(ESType, Hql.string):
        ...
    
    @register_type('elasticsearch_object') 
    class object(ESType, Hql.object):
        ...
    
    @register_type('elasticsearch_flattened') 
    class flattened(ESType, Hql.object):
        ...
        
    @register_type('elasticsearch_nested')
    class nested(ESType, Hql.object):
        ...
    
    @register_type('elasticsearch_alias') 
    class alias(ESType, Hql.string):
        def __init__(self):
            logging.warn("Elasticsearch type 'alias' not implemented at the moment")
            ESTypes.ESType.__init__(self)
        
    @register_type('elasticsearch_point')
    class point(ESType, Hql.multivalue):
        def __init__(self):
            ESTypes.ESType.__init__(self)
            Hql.multivalue.__init__(self, Hql.float)
        
    @register_type('elasticsearch_geo_point')
    class geo_point(ESType, Hql.multivalue):
         def __init__(self):
            ESTypes.ESType.__init__(self)
            Hql.multivalue.__init__(self, Hql.float)
    
    @register_type('elasticsearch_shape') 
    class shape(ESType, Hql.matrix):
        def __init__(self):
            ESTypes.ESType.__init__(self)
            Hql.matrix.__init__(self, Hql.float)
                    
    @register_type('elasticsearch_geo_shape')   
    class geo_shape(ESType, Hql.matrix):
        def __init__(self):
            ESTypes.ESType.__init__(self)
            Hql.matrix.__init__(self, Hql.float)