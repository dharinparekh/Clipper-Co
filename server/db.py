
import MySQLdb
import json
from datetime import datetime
import pyotp
import random
import time

USERNAME = 'xxx'
HOST = 'xxx'
PASSWORD = 'xxx'
DB = 'xxx'

SECRET = pyotp.random_base32()

conn = MySQLdb.connect(HOST,USERNAME,PASSWORD,DB)
conn.ping(True)
ERROR = json.dumps({"status":0,"message":"mysql error"})
htotp = pyotp.HOTP(SECRET)
a = range(1,1000)


#authenticate user
def auth(uname,pwd):
    #print uname, pwd
    #print "++++++++++++++++++++++++++++++++=="
    query = "Select * from users where uname='"+uname+"' and pwd='"+pwd+"'"
    curr = conn.cursor()
    try:
        curr.execute(query)
    except Exception as e:
        conn.rollback()
        print e
        return ERROR
    data = curr.fetchall()
    #print "-----------------------"
    #print data
    if(len(data)!=1):
        return json.dumps({"status":False,"message":"user doesn't exist"})
    else:
        return json.dumps({"status":True, 'message':"logged in successfully"})

def insert(uname,pwd):
    val = json.loads(auth(uname,pwd))
    if(val['message']=='mysql error'):
        return ERROR
    if(val['status']==True):
        return json.dumps({"status":False,"message":"the user already exists"})
    else:
        timeNow = datetime.now()
        query = "Insert into users (uname,pwd,date_time,counter) values ('"+uname+"','"+pwd+"','"+str(timeNow)+"',"+str(-1)+");"
        curr = conn.cursor()
        try:
            curr.execute(query)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print e
            return ERROR
        return json.dumps({"status":True, "message":"user successfully entered"})
    # return json.dumps({"status":False, "message":"some error occured"})

def _generate_otp(counter):
    return htotp.at(int(counter))

def _get_counter():
    b = a[random.randint(0,len(a))]
    a.remove(b)
    return b

def get_otp(uname,pwd,type):
    counter = _get_counter()
    otp = _generate_otp(counter)
    time_now = datetime.now()
    query = "update users set otp_type= "+str(type)+", counter= "+str(counter)+","+"stamp= '"+str(time_now)+"', otp = "+str(otp)+" where uname= '"+uname+"' and pwd= '"+pwd+"'"
    curr = conn.cursor()
    try:
        curr.execute(query)
        conn.commit()
    except Exception as e:
        conn.rollback()
        print e
        return ERROR
    return json.dumps({"status":1,"otp":otp})


def check_otp(otp):
    query = "select * from users where otp = "+str(otp)
    curr = conn.cursor()
    try:
        curr.execute(query)
    except Exception as e:
        print e
        return ERROR
    data = curr.fetchall()
    if len(data)!=1:
        return json.dumps({"status":0,"topic":0,"message":"wrong otp"})
    else:
	#return  topic via joining username and pw
	time_stored = data[0][-2]
	type  = data[0][-1]
	time_now = datetime.now()
	if(type==1):
		topic = "/"+str(otp)
	else:
	        topic = str(data[0][1])+'/'+str(data[0][2])+"/cc"
	time_diff = time_now - time_stored
        return json.dumps({"status":1,"diff":time_diff.total_seconds() ,"topic":topic,"message":"matched"})
    return ERROR

def delete_otp(uname,pwd):

	query = "update users set otp= -1 where uname = '"+uname+"' and pwd = '"+pwd+"'"
	print query
	curr = conn.cursor()
	try:
		curr.execute(query)
		conn.commit()
	except Exception as e:
		print e
		return ERROR
