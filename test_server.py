#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer


class web_server(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)

        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))


def run():
    print('starting server at localhost:8080')
    server_address = ('127.0.0.1', 8080)
    httpd = HTTPServer(server_address, web_server)
    print('running server...')
    httpd.serve_forever()


run()
