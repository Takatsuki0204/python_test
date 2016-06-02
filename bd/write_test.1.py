#! /usr/bin/env python
# encoding: utf-8

import sqlite3

#db = "C:\Users\TAKATSUKI\Documents\環境BOX\sqlite_db\environment.db"
#connector = sqlite3.connect(db)

class db:
    def __init__(self, dbname):
        self.dbname = dbname
        self.connector = sqlite3.connect(dbname)
        
    def create_table(self):
        sql = "CREATE TABLE IF NOT EXISTS test(id, name, value)"
        self.connector.execute(sql)
        self.connector.commit()

    def put_data(self, dict):
        with self.connector:
            self.connector.execute("INSERT INTO test VALUES (:id, :name, :value)", dict)

if __name__ == "__main__":
    dbn = "C:\Users\TAKATSUKI\Documents\環境BOX\sqlite_db\environment.db"
    database = db(dbn)
    database.create_table()
    
    dict = {"id": 1, "name": "python", "value": 12345}
    database.put_data(dict)