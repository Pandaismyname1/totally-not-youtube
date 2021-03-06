import http.server
from http import HTTPStatus
import socketserver
import os
import cgitb

port = 8080
ip = '127.0.0.1'

cgitb.enable()
Handler = http.server.CGIHTTPRequestHandler

with socketserver.TCPServer((ip, port), Handler) as httpd:
    print("serving at port", port)
    httpd.server_name = "test"
    httpd.server_port = port
    httpd.serve_forever()
