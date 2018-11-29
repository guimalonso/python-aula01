from pymongo import MongoClient
from psycopg2 import connect as cn

def mongo_connect(base):
    con = MongoClient()
    return con[base]

def psy_connect(user, pw, base):
    con = cn("host=localhost user={} password={} dbname={}".format(
        user, pw, base
    ))
    return con.cursor()
