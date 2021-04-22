import http.server
import socketserver
import os

PORT = os.environ.get('PORT',8080)
class CustomRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        with open('index.html' ,'rb') as f:
            self.send_response(200)
            self.send_header('Content-type','text/html; charset=uft-8')
            self.end_headers()
            self.wfile.write(f.read())


try:
    httpd = socketserver.TCPServer(("",int(PORT)), CustomRequestHandler)
    print("Python webserver listening at port {} ".format(PORT))
    httpd.serve_forever()
except Exception as err:
    print ("Http Exception ")
