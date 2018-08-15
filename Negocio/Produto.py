#!/usr/bin/python

import Dados.ProdutoBD


class Produto:

    def cadastrar(self, descricao, categoria, fornecedor, unidade, agora, obs):
        oObjetoBD = Dados.ProdutoBD.ProdutoBD ()

        return oObjetoBD.cadastrar (descricao, categoria, fornecedor, unidade, agora, obs)

    def selecionar(self):
        oObjetoBD = Dados.ProdutoBD.ProdutoBD ()

        return oObjetoBD.selecionar ()
