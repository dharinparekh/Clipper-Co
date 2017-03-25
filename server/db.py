
import MySQLdb
import json
from datetime import datetime
import pyotp
import random


USERNAME = 'XXX'
HOST = 'xxx'
PASSWORD = 'xxx'
DB = 'xxx'

SECRET = pyotp.random_base32()

conn = MySQLdb.connect(HOST,USERNAME,PASSWORD,DB)
conn.ping(True)
ERROR = json.dumps({"status":False,"message":"mysql error"})
htotp = pyotp.HOTP(SECRET)
a = range(1,1000)


#authenticate user
def auth(uname,pwd):
    query = "Select * from users where uname='"+uname+"' and pwd='"+pwd+"'"
    curr = conn.cursor()
    try:
        curr.execute(query)
    except Exception as e:
        conn.rollback()
        print e
        return ERROR
    data = curr.fetchall()
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
        query = "Insert into users (uname,pwd,date_time) values ('"+uname+"','"+pwd+"','"+str(timeNow)+"')"
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

def get_otp(uname,pwd):
    counter = _get_counter()
    otp = _generate_otp(counter)
    query = "update users set counter= "+str(counter)+","+"otp = "+str(otp)+" where uname= '"+uname+"' and pwd= '"+pwd+"'"
    curr = conn.cursor()
    try:
        curr.execute(query)
        conn.commit()
    except Exception as e:
        conn.rollback()
        print e
        return ERROR
    return json.dumps({"status":True,"otp":otp})


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
        return json.dumps({"status":False,"topic":None,"message":"wrong otp"})
    else:
	#return  topic via joining username and pwd
        topic = str(data[0][1])+'/'+str(data[0][2])+"/cc"
        return json.dumps({"status":True,"topic":topic,"message":"matched"})
    return ERROR
