from datetime import datetime
import os, json
from http.server import HTTPServer, BaseHTTPRequestHandler
from functions import fetch_id,fetch_unit,fetch_rainfall_status,env_check,fetch_api_data

HOST = "0.0.0.0"
PORT = 8080

class NeuralHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        # self.send_header("Content-type", "text/csv")
        api_url = env_check("API_URL")
        location = env_check("LOCATION")
    
        data = fetch_api_data(api_url)
        unit = fetch_unit(data)
        station_id = fetch_id(data, location)
        status = fetch_rainfall_status(data, station_id)
    
        current_date_time = datetime.now()
        current_time = current_date_time.strftime("%H:%M")
    
        rainfall_amt = str(status[1])+unit
        raining_status = status[0]
    
        print_value = location+', '+current_time+', '+rainfall_amt+', '+raining_status
        print(print_value)

        self.end_headers()
        #self.wfile.write(("<html><body><h4>Upper Changi Road North, 16:19, 0.2mm, Raining</h4></body></html>".encode()))
        #self.wfile.write(("Upper Changi Road North, 16:19, 0.2mm, Raining".encode()))

        self.wfile.write(print_value.encode())


server = HTTPServer((HOST, PORT), NeuralHTTP)
print("Rainfall Service started",'\n')

server.serve_forever()
server.server_close()
Print("Server stopped")