#! /usr/bin/env python
# encoding: utf-8

import sqlite3

db = "C:\Users\TAKATSUKI\Documents\環境BOX\sqlite_db\environment.db"
connector = sqlite3.connect(db)

def read_data():
    cur = connector.execute("SELECT * FROM test")
    apps = [app for app in cur.fetchall()]
    for i in apps:
        print(i)

if __name__ == "__main__":
    read_data()