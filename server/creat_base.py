import os
from subprocess import Popen,PIPE
from connect import get_conn
from config import debug, host,port, user, passwd,db
prefix=os.path.split(os.path.realpath(__file__))[0]

def creat_table():
    try:
    	conn=get_conn()
	conn.close()
    except:
  	print "connection error"
	return False

    
    sql='source '+str(prefix)+ '/creat_tables.sql;'
    sql2='source '+str(prefix)+ '/buildtag.sql;'
    try:
	Popen('mysql -h%s -P%s -u%s -p%s -D%s'  %(host, port, user, passwd, db), stdout=PIPE, stdin=PIPE, shell=True).communicate(input=sql+sql2)



    except:
	print 'build table error'
	return False
    print 'build basic table successfully'
    return True

if debug:
    creat_table()
