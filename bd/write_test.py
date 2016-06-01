#! /usr/bin/env python
# encoding: utf-8

import sqlite3

if __name__ == "__main__":
    connector = sqlite3.connect("C:\Users\TAKATSUKI\Documents\環境BOX\sqlite_db\environment.db")
    
    sql = "create table if not exists test_2(id, name)"
    connector.execute(sql)
    
    sql = "insert into test_2 values('1', 'python')"
    connector.execute(sql)
    sql = "insert into test_2 values('2', 'パイソン')"
    connector.execute(sql)
    sql = "insert into test_2 values('3', 'ぱいそん')"
    connector.execute(sql)
    
    connector.commit()
    connector.close()