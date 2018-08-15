#!/usr/bin/python3.6

from urllib.parse import urlencode

try:
    u = Produto ()

    u.cadastrar (descricao, categoria, fornecedor, unidade, agora, obs)

    print('Location: cadastrar.py?' + urlencode ({'msg': 'Produto cadastrado!'}))
    print()

except Exception:
    print('Location: cadastrar.py?' + urlencode ({'msg': 'Erro ao cadastrar'}))
