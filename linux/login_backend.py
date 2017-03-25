###!/usr/bin/python           # This is client.py file
print "Connecting to another server"
import paho.mqtt.client as mqtt
import json

val = False
flag = False
otp_flag = False
check_otp_flag = False
otp = None
otp_topic = None
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code in login backend"+str(rc))

def on_message_callback(client, userdata, msg):
    global flag, val, otp_flag, otp, check_otp_flag, otp_topic
    print msg.topic+":- "+msg.payload
    val = "true" in msg.payload
    if "/otp" in msg.topic:
        otp_flag = True
        otp = msg.payload
    elif "checkotp" in msg.topic:
        check_otp_flag = True
        otp_topic = msg.payload
    else:
        flag = True

    #add this data to clipboard
    # print type(msg)

def login(Username,Password):
    global flag, val
    client.subscribe(Username+"/"+Password)
    client.publish("/register",Username+"/"+Password)
    while not flag:
        pass
    print "Done"
    if val:
        #client.disconnect() should disconnect
        print "Hello"
    else:
        flag = False
    return val

def register(Username,Password):
    client.subscribe(Username+"/"+Password)
    client.publish("/signup",Username+"/"+Password)

def requestotp():
    global otp_flag
    #client.connect("139.59.79.171")
    data = open('credentials.txt','r').read().split('\n')
    Username,pwd = data
    client.subscribe(Username+"/"+pwd+"/otp")
    client.publish("/requestotp",Username+"/"+pwd)
    #client.disconnect()
    while not otp_flag:
        pass
    otp_flag = False
    otp_data = eval(otp)
    otp_num = otp_data["otp"]
    return otp_num

def checkotp(otp):
    global check_otp_flag
    #client.connect("139.59.79.171")
    data = open('credentials.txt','r').read().split('\n')
    if(len(data)>=2):
        Username,pwd = data[:2]
    else:
        print "credentials file empty"
    client.subscribe("/checkotp"+Username+"/"+pwd)
    client.publish("/checkotp",Username+"/"+pwd+"/"+otp)
    while not check_otp_flag:
        pass
    check_otp_flag = False
    otp_topic_data = eval(otp_topic)
    otp_t = otp_topic_data["topic"]
    time = int(otp_topic_data["diff"])
    if otp_t == '0' or otp_t == 0:
        return "error/error", 0
    return otp_t, time

def invalidateotp():
    data = open('credentials.txt','r').read().split('\n')
    if(len(data)>=2):
        Username,pwd = data[:2]
    else:
        print "credentials file empty"
    client.publish("/invalidate",Username+"/"+pwd)
    
def on_disconnect():
    reconnect()
    
client = mqtt.Client()
#client.username_pw_set("admin", "Jk9821005717")
client.connect("139.59.79.171")
client.on_connect = on_connect
client.on_message = on_message_callback
client.on_disconnect = on_disconnect
client.loop_start()
