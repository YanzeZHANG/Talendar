import os, linecache, MySQLdb 
from DBUtils.PooledDB import PooledDB
from config import host, user, passwd, db, charset

prefix=os.path.split(os.path.realpath(__file__))[0]

class Pool(object):
    def __init__(self):
	self.pool=PooledDB(MySQLdb,5,host=host,user=user,passwd=passwd,db=db,charset=charset,cursorclass = MySQLdb.cursors.DictCursor)

    def get_pool(self):
	return self.pool

def get_conn():
    return Pool().get_pool().connection()
