import os
import pymysql
from connect import get_conn
from subprocess import Popen, PIPE
from config import debug,host,port,user,passwd,db

prefix=os.path.split(os.path.realpath(__file__))[0]

class user(object):
    def __init__(mailbox):
	self.ID=None
	self.mailbox=mailbox
	self.username=None
    def login(mailbox,passwd):
	cursor=get_conn().cursor()
	sql='SELECT userid, username, passwd FROM userinfo'
	cursor.execute(sql)
	if cursor['userid']==None:
	    print 'user not exists'
	    return 0
	elif not cursor['passwd']==passwd:
	    return -1
	else:
	    self.ID=cursor.userid
	    self.username=cursor.username
	    return 1
	
    def create_new(username,mailbox,passwd_new):

print
