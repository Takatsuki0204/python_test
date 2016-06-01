#! /usr/bin/env python
# encoding: utf-8

import sqlite3

db = "C:\Users\TAKATSUKI\Documents\環境BOX\sqlite_db\environment.db"
connector = sqlite3.connect(db)

def create_table():
    sql = "CREATE TABLE IF NOT EXISTS test(id, name, value)"
    connector.execute(sql)
    connector.commit()

def put_data(dict):
    with connector:
        connector.execute("INSERT INTO test VALUES (:id, :name, :value)", dict)

if __name__ == "__main__":
    create_table()
    
    dict = {"id": 1, "name": "python", "value": 12345}
    put_data(dict)