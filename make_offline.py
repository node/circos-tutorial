#!/usr/bin/env python


# step 1 : create new index.html
print '>>> create new index.html'
import os
pwd = os.getcwd()
file_content = '''<html>
<head>
<title>Redirect to index ...</title>
<meta http-equiv="Content-Language" content="zh-CN">
<meta HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<meta http-equiv="refresh" content="0.1;url=/documentation/tutorials/index.html">
</head>
<body>
</body>
</html>'''
filename = 'circos.ca/index.html'
f = open(filename,'w')
f.write(file_content)
f.flush()
f.close()

# step 2 : update fonts and jsapi from google
print '>>> generate local google fonts and jsapi files '
pass


print '    update fonts and jsapi files url'
# TODO 

# step 3 : start local simple http server with port 8000
print '>>> startup local simple http server with port 8000'

os.chdir(pwd + '/circos.ca')
import SimpleHTTPServer
import SocketServer
PORT = 8000
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)
print ">>> Visit http://localhost:%d   " %(PORT)
print '    Use Ctrl+c to shutdown.'
httpd.serve_forever()

#end 