from datetime import datetime
import os
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from test_functions import fetch_api_data,fetch_id,fetch_unit,fetch_rainfall_status,test_raining

HOST = "0.0.0.0"
PORT = 8080

class NeuralHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        # self.send_header("Content-type", "text/csv")
        self.end_headers()
        self.wfile.write(("<html><body><h4>Upper Changi Road North, 16:19, 0.2mm, Raining</h4></body></html>".encode()))
        #self.wfile.write(("Upper Changi Road North, 16:19, 0.2mm, Raining".encode()))


server = HTTPServer((HOST, PORT), NeuralHTTP)
print("Server running now..")

server.serve_forever()
server.server_close()
Print("Server stopped")