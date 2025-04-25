import json
from http.server import HTTPServer, BaseHTTPRequestHandler

def retmsg(msg:str, level:str):
    msg = {
        'Message': msg,
        'Level': level
    }
    
    return json.dumps(msg).encode()

run = True

class Server(HTTPServer):
    def __init__(self, server_address, RequestHandlerClass):
        super().__init__(server_address, RequestHandlerClass)
        self.post_data = {}

class Listener(BaseHTTPRequestHandler):
    def do_POST(self):        
        nbytes = int(self.headers.get('Content-Length', 0))
        
        self.server.post_data = {
            'origin': '',
            'rows': []
        }
                
        if nbytes == 0:
            self.send_response(204)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(retmsg('No content', 'INFO'))
            return
        
        # read data input
        inbytes = self.rfile.read(nbytes).decode('utf-8')
         
        try:
            self.server.post_data = json.loads(inbytes)
        except json.JSONDecodeError as e:
            self.send_response(400)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(retmsg(str(e), 'CRITICAL'))
            return

        if 'rows' not in self.server.post_data:
            self.send_response(400)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(retmsg('Missing rows', 'CRITICAL'))
            return

        # Respond with a success message
        self.send_response(202)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(retmsg('OK', 'INFO'))