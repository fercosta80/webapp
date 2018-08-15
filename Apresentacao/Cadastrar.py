#!/usr/bin/python3.6


import Negocio.Produto

import sys, cgi, cgitb

# sys.path.append('/srv/www/cgi-bin/webapp/')
sys.path.append ('/home/fernando/cgi-bin/webapp/')

cgitb.enable ()

p = Negocio.Produto.Produto ()

ret = p.selecionar ()

v = cgi.FormContentDict ()

print ('Content-Type: text/html')

print ('<html>')

print ('<head>')

print ('<title>Cadastro de produto</title>')

print ('</head>')
print ('</html>')
