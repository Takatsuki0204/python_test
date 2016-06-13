#! /usr/bin/env python
# encoding: utf-8

import MySQLdb, datetime
import numpy.random as nprand

class db:
    def __init__(self, ip, dbn, usern, pw, char="utf8"):
        self.connector = MySQLdb.connect(host=ip, db=dbn, user=usern, passwd=pw, charset=char)
        self.cursor = self.connector.cursor(MySQLdb.cursors.DictCursor)
    
    def closed(self):
        self.connector.close()
    
    def create_table(self, sql):
        self.cursor.execute(sql)
        self.connector.commit()

if __name__ == "__main__":
    hostip = "192.168.10.91"
    dbn = "db_test"
    usern = "user1"
    pw = "Asdeng"
    database = db(hostip, dbn, usern, pw)
    table = "CREATE TABLE IF NOT EXISTS environment(datetime timestamp, temp float, humidity int)"
    database.create_table(table)

    now = datetime.datetime.now()
    temp = nprand.uniform(20, 40)
    rh = nprand.randint(40, 70)

    sql = ("INSERT INTO environment VALUES('%s', '%.2f', '%d')" % (str(now), temp, rh))
    database.create_table(sql)