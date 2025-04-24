from elasticsearch import Elasticsearch
import logging
import json
import time

# Get our config file
with open('./conf.json', mode='r') as f:
    conf = json.loads(f.read())

# Host, or hosts, to use for the query.
# Should be in array format
ELASTIC_HOSTS = conf.get('ELASTIC_HOSTS', ['http://localhost:9200'])
# Elastic user to use
ELASTIC_USER = conf.get('ELASTIC_USER', 'elastic')
# Elastic user password to use
ELASTIC_PASS = conf.get('ELASTIC_PASS', 'changeme')
# SSL Validation
VALIDATE_CERTS = conf.get('VALIDATE_CERTS', 'true')
# How long should the scroll session be kept alive?
SCROLL_TIME = conf.get('SCROLL_TIME', '1m')
# How many rows should we scroll per scroll?
# Max is 10000
SCROLL_SIZE = conf.get('SCROLL_SIZE', 10000)
# Request timeout in seconds
TIMEOUT = conf.get('TIMEOUT', 10)

# Debug?
DEBUG = conf.get('DEBUG', False)

# Get the query
QUERY = conf.get('QUERY', { 'match_all': {} })
# Get the Index
INDEX = conf.get('INDEX', '*')

if DEBUG:
    logging.getLogger().setLevel(logging.DEBUG)
else:
    logging.getLogger().setLevel(logging.CRITICAL)

# Make a scrolling query to Elasticsearch
# Default safety limit is 100000 queries to be returned
def make_query(index:str, query:dict, limit:int=100000):
    client = Elasticsearch(
        ELASTIC_HOSTS,
        basic_auth=(ELASTIC_USER, ELASTIC_PASS),
        verify_certs=VALIDATE_CERTS,
        request_timeout=TIMEOUT,
        retry_on_timeout=True
    )
    
    logging.debug("Starting initial query")

    res = client.search(
        index=index,
        size=SCROLL_SIZE,
        scroll=SCROLL_TIME,
        query=query,
    )
    sid = res['_scroll_id']
    
    logging.debug("Start scrolling")
    
    # Will scroll through until we reach our limit, or no more results.
    # Enables the take operator
    remainder = limit
    result_count = 0
    results = []
    while result_count < limit:
        logging.debug(f"Scroll {result_count} < {limit} max")
        
        if len(res['hits']['hits']) == 0:
            logging.debug(f"No more results to evaluate")
            logging.debug(f"Timed out? {res['timed_out']}")
            break
        
        # Ensure that we only print the number of remaining rows
        [print(json.dumps(x)) for x in res['hits']['hits'][:remainder]]
        result_count += len(res['hits']['hits'][:remainder])
        
        remainder = limit - result_count
        
        res = client.scroll(
            scroll_id=sid,
            scroll=SCROLL_TIME,
        )

    client.clear_scroll(scroll_id=sid)

    return results


def main():
    start = time.perf_counter()
    
    make_query(INDEX, QUERY)
    
    end = time.perf_counter()
    logging.debug(f'Query took {end - start} seconds')
    
if __name__ == "__main__":
    main()