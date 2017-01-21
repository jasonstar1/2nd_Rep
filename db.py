# -*- coding:utf-8 -*-  
import sys
import bottle
import psycopg2

# 数据库连接参数


def testdb(sql):
    conn = psycopg2.connect(database="blogdb", user="postgres", password="123456", host="localhost", port="5432")
    cur = conn.cursor()
    # cur.execute("CREATE TABLE test(id serial PRIMARY KEY, num integer,data varchar);")
    # insert one item
    cur.execute(sql)    # all rows in table
    conn.commit()
    cur.close()
    conn.close()
    return '1'

def testdb1(sql):
    conn = psycopg2.connect(database="blogdb", user="postgres", password="123456", host="localhost", port="5432")
    cur = conn.cursor()
    # cur.execute("CREATE TABLE test(id serial PRIMARY KEY, num integer,data varchar);")
    # insert one item
    try:
        cur.execute(sql)
    except:
        return []
    rows=cur.fetchall()     # all rows in table
    conn.commit()
    cur.close()
    conn.close()
    return rows

def Arg(arg):
    arg = bytes(arg, encoding="ISO8859-1")
    arg = str(arg, encoding="utf-8")
    return arg
