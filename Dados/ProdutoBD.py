#!/usr/bin/python

import BD


class ProdutoBD:

    def __init__(self):
        self.oConexao = BD ()

    def cadastrar(self, descricao, categoria, fornecedor, unidade, agora, obs):
        sql = "INSERT INTO produto SET descricao = '" + descricao + "', categoria = '" + categoria + "', fornecedor='" + fornecedor + "',unidade = '" + unidade + "', data = '" + agora + "', obs = '" + obs + "'"

        self.oConexao.conn.execute (sql)

        self.oConexao.bd.commit ()

        return ""

    def selecionar(self):
        sql = "SELECT * FROM produto ORDER BY descricao ASC"

        self.oConexao.conn.execute (sql)

        r = self.oConexao.conn.fetchall ()

        self.oConexao.Close ()

        return r
