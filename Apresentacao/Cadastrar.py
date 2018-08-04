#!/usr/bin/python

from urllib.parse import urlencode

from Negocio.Produto import Produto
 
import sys, cgi, cgitb

sys.path.append('/srv/www/cgi-bin/webapp/')


cgitb.enable()
 
p = Produto()
 
ret = p.selecionar()
 
v = cgi.FormContentDict()
 
print ('Content-Type: text/html')
 

print('<html>')
  
print('<head>')
 
print('<title>Cadastro de produto</title>')
 
print('</head>')
print('</html>')