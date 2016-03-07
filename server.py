#!/usr/bin/env python
import SimpleHTTPServer
import SocketServer
class myHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
    	print self.path
	if self.path == '/a.html':
	    self.send_response(302)
       	    self.send_header('Location','http://130.126.141.156/b.html')
       	    self.end_headers()
	if self.path == '/b.html':
   	    f = open('/home/scion/SimpleRedirect/b.html')
            #send code 200 response
            self.send_response(200)
	    #send header first
            self.send_header('Content-type','text-html')
            self.end_headers()
            #send file content to client
            self.wfile.write(f.read())
            f.close()
	    

PORT = 80
handler = SocketServer.TCPServer(("", PORT), myHandler)
print "serving at port 80"
handler.serve_forever()
