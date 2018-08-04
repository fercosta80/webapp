#!/usr/bin/python

try: 
  
   u = Produto()  
 
   u.cadastrar(descricao,categoria,fornecedor,unidade,agora,obs)
 
   print ('Location: cadastrar.py?'+urlencode({'msg':'Produto cadastrado!'}))
   print()
 
except:
 
   print ('Location: cadastrar.py?'+urlencode({'msg':'Erro ao cadastrar'})
   print()