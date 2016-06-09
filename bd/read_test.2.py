#! /usr/bin/env python
# encoding: utf-8

import MySQLdb

if __name__ == "__main__":
    connector = MySQLdb.connect(host="192.168.10.91", db="db_test", user="user1", passwd="Asdeng", charset="utf8")
    cursor = connector.cursor()
    cursor.execute("select * from environment")

    print cursor.fetchall

    cursor.close()
    connector.close()