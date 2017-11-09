import os
from subprocess import Popen, PIPE
from config import debug, host, port, user, passwd, db

prefix=os.path.split(os.path.realpath(__file__))[0]

def add_new_user(username,mailbox, passwd_new):#create a new user;add_new_user(string,string,string)
    try:
	Popen('mysql -h%s -P%s -u%s -p%s -D%s' %(host, port, user, passwd, db), stdout=PIPE, stdin=PIPE, shell=True).communicate(input='CREATE USER \'%s\'@\'%s\' IDENTIFIED BY \'%s\';INSERT INTO user_info(username,mailbox,passwd) VALUES (\'%s\', \'%s\', \'%s\');commit;' %(mailbox, host, passwd_new,username,mailbox, passwd_new))
	
	print 'successed'
	return True
    except :
	print "Failed to insert new user"
	return False

def rmuser(mailbox):#delete user whose mailbox=mailbox;rmuser(string)
    try:
	Popen('mysql -h%s -P%s -u%s -p%s -D%s' %(host, port, user, passwd, db), stdout=PIPE, stdin=PIPE, shell=True).communicate(input='DROP USER \'%s\'@\'%s\';DELETE FROM student_info WHERE (student_info.userid in (SELECT userid FROM user_info WHERE (mailbox=\'%s\')));DELETE FROM user_info WHERE (user_info.mailbox=\'%s\') ; GRANT SELECT,INSERT ON %s.works TO \'%s\'@\'%s\';GRANT SELECT,' %(mailbox, host, mailbox,mailbox,db,mailbox,host)) 
	print 'delete successfully'
	return True
    except :
	print 'fail to delete %s'%(mailbox)
	return False


def insert_student(mailbox,stdid,info_passwd): #insert student id and passwd. safety problem;insert_student(string,string,string)
    hhhh

if debug:
    add_new_user('test1','xuecheng','123')
    rmuser('xuecheng')
