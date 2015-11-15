#!python2.7
# coding=UTF-8

# info TODO

__author__ = 'sumrise'

import practice1
import MySQLdb

db = MySQLdb.connect("localhost", "", "", "python_practice")

cursor = db.cursor()

print()
for i in range(200):
    code = practice1.generator()
    sql = 'insert into practice2(id,code) VALUES ("%d","%s")' % \
          (db.insert_id(), code)
    print(code)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

db.close()

print ""
