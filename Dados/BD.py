#!/usr/bin/python3.6

import pymysql


class BD:

    def __init__(self):
        self.bd = pymysql.connect (host="localhost", port=3306, user="root", passwd="fsmg", db="appweb")
        self.conn = self.bd.cursor()

    def Close(self):
        self.conn.close ()
