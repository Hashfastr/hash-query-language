from HqlConnector import Server, Listener
import logging
import json

# Get our config file
with open('./conf.json', mode='r') as f:
    conf = json.loads(f.read())
    
FIELDS = conf.get('FIELDS', [])
TYPE = conf.get('TYPE', 'project')

# Debug?
DEBUG = conf.get('DEBUG', False)

if DEBUG:
    logging.getLogger().setLevel(logging.DEBUG)
else:
    logging.getLogger().setLevel(logging.CRITICAL)

def project(data:list, ptype:str, fields:list):    
    if ptype == "project":
        projected = df[fields]
    else:
        print("uh oh, unhandled project type")
        return []
    
    return projected.to_dict(orient='records')

def main():
    address = ('', 8080)
    server = Server(address, Listener)

    # Init request
    server.handle_request()
    
    # Loop until we don't have any data left
    while len(server.post_data['rows']):
        data = project(server.post_data['rows'], TYPE, FIELDS)
        
        print(json.dumps(data, indent=2))

        server.handle_request()
        
    server.server_close()
        
    pass
    
if __name__ == "__main__":
    main()