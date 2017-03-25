
import MySQLdb
import json
from datetime import datetime
import pyotp
import random


USERNAME = 'root'
HOST = '127.0.0.1'
PASSWORD = 'tiger'
DB = 'hackathon'

conn = MySQLdb.connect(HOST,USERNAME,PASSWORD,DB)
conn.ping(True)
ERROR = json.dumps({"status":False,"message":"mysql error"})

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
