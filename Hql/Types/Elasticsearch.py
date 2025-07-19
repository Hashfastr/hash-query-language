from Hql.Types import HqlTypes as hqlt
import logging

from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import register_type, get_type
# from ..Types.Compiler import CompilerType

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

        def __len__(self):
            return 1
    
    @staticmethod
    def from_name(name:str):
        return get_type(f'elasticsearch_{name}')
            
    @register_type('elasticsearch_scaled_float')
    class scaled_float(ESType, hqlt.decimal):
        ...

    @register_type('elasticsearch_half_float')
    class half_float(ESType, hqlt.float):
        ...
    
    @register_type('elasticsearch_float') 
    class float(ESType, hqlt.float):
        ...
        
    @register_type('elasticsearch_double')
    class double(ESType, hqlt.double):
        ...
    
    @register_type('elasticsearch_byte') 
    class byte(ESType, hqlt.byte):
        ...
    
    @register_type('elasticsearch_short') 
    class short(ESType, hqlt.short):
        ...
    
    @register_type('elasticsearch_integer') 
    class integer(ESType, hqlt.int):
        ...
    
    @register_type('elasticsearch_long') 
    class long(ESType, hqlt.long):
        ...
    
    @register_type('elasticsearch_unsigned_long') 
    class unsigned_long(ESType, hqlt.ulong):
        ...
    
    @register_type('elasticsearch_ip') 
    class ip(ESType, hqlt.string):
        ...
        
    @register_type('elasticsearch_date')
    class date(ESType, hqlt.datetime):
        ...
    
    @register_type('elasticsearch_date_nanos') 
    class date_nanos(ESType, hqlt.datetime):
        ...
        
    @register_type('elasticsearch_date_range')
    class date_range(ESType, hqlt.range):
        def __init__(self):
            ESTypes.ESType.__init__(self)
            hqlt.range.__init__(self, hqlt.datetime)
    
    @register_type('elasticsearch_integer_range') 
    class integer_range(ESType, hqlt.range):
        def __init__(self):
            ESTypes.ESType.__init__(self)
            hqlt.range.__init__(self, hqlt.datetime)

    @register_type('elasticsearch_float_range')
    class float_range(ESType, hqlt.range):
        def __init__(self):
            ESTypes.ESType.__init__(self)
            hqlt.range.__init__(self, hqlt.datetime)
        
    @register_type('elasticsearch_long_range')   
    class long_range(ESType, hqlt.range):
        def __init__(self):
            ESTypes.ESType.__init__(self)
            hqlt.range.__init__(self, hqlt.datetime)
        
    @register_type('elasticsearch_double_range') 
    class double_range(ESType, hqlt.range):
        def __init__(self):
            ESTypes.ESType.__init__(self)
            hqlt.range.__init__(self, hqlt.datetime)

    @register_type('elasticsearch_ip_range') 
    class ip_range(ESType, hqlt.range):
        def __init__(self, ip_type:int):
            ESTypes.ESType.__init__(self)
            
            if ip_type not in (4, 6):
                raise hqle.CompilerException(f"Invalid IP version type {ip_type} passed to Elasticsearch type")
            
            if ip_type == 4:
                hqlt.range.__init__(self, type=hqlt.ip4)
            else:
                hqlt.range.__init__(self, type=hqlt.ip6)
    
    @register_type('elasticsearch_keyword') 
    class keyword(ESType, hqlt.string):
        ...
    
    @register_type('elasticsearch_constant_keyword') 
    class constant_keyword(ESType, hqlt.string):
        ...
    
    @register_type('elasticsearch_wildcard') 
    class wildcard(ESType, hqlt.string):
        ...
    
    @register_type('elasticsearch_binary') 
    class binary(ESType, hqlt.string):
        ...
    
    @register_type('elasticsearch_object') 
    class object(ESType, hqlt.object):
        ...
    
    @register_type('elasticsearch_flattened') 
    class flattened(ESType, hqlt.object):
        ...
        
    @register_type('elasticsearch_nested')
    class nested(ESType, hqlt.object):
        ...
    
    @register_type('elasticsearch_alias') 
    class alias(ESType, hqlt.string):
        def __init__(self):
            logging.warn("Elasticsearch type 'alias' not implemented at the moment")
            ESTypes.ESType.__init__(self)
        
    @register_type('elasticsearch_point')
    class point(ESType, hqlt.multivalue):
        def __init__(self):
            ESTypes.ESType.__init__(self)
            hqlt.multivalue.__init__(self, hqlt.float)
        
    @register_type('elasticsearch_geo_point')
    class geo_point(ESType, hqlt.multivalue):
         def __init__(self):
            ESTypes.ESType.__init__(self)
            hqlt.multivalue.__init__(self, hqlt.float)
    
    @register_type('elasticsearch_shape') 
    class shape(ESType, hqlt.matrix):
        def __init__(self):
            ESTypes.ESType.__init__(self)
            hqlt.matrix.__init__(self, hqlt.float)
                    
    @register_type('elasticsearch_geo_shape')   
    class geo_shape(ESType, hqlt.matrix):
        def __init__(self):
            ESTypes.ESType.__init__(self)
            hqlt.matrix.__init__(self, hqlt.float)
