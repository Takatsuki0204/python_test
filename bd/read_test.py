#! /usr/bin/env python
# encoding: utf-8

import sqlite3

if __name__ == "__main__":
    connector = sqlite3.connect("C:\Users\TAKATSUKI\Documents\環境BOX\sqlite_db\environment.db")
    cursor = connector.cursor()
    cursor.execute("select * from test")
    
    result = cursor.fetchall()
    
    for row in result:
        print "===== Hit! ====="
        print "code -- " + unicode(row[0])
        print "name -- " + unicode(row[0])
    
    cursor.close()
    connector.close()