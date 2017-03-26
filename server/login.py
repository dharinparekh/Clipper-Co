import paho.mqtt.client as mqtt
from db import *

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_message_callback(client, userdata, msg):
    #goto(msg.topic,msg.payload)
    topic = msg.topic
    message = msg.payload
    print "I received message as: "+message
#    print "Username: "+message.split('/')[0]+" Password: "+message.split('/')[1]
    #print "Username: "+message.split('/')[1]+" Password: "+message.split('/')[2]
    if("register" in topic):
        Username = message.split('/')[0]
        Password = message.split('/')[1]
        result = auth(Username,Password)
        print result
        client.publish(message,result)
    elif("signup" in topic):
        Username = message.split('/')[0]
        Password = message.split('/')[1]
        result = insert(Username,Password)
        print result
        client.publish(message,result)
    elif("requestotp" in topic):
        Username = message.split('/')[0]
        Password = message.split('/')[1]
        value = message.split('/')[2]
        result = get_otp(Username,Password,value)
        client.publish(Username+"/"+Password+"/otp",result)
    elif("checkotp" in topic):
        print "OTP check:- ",message
        Username = message.split('/')[0]
        Password = message.split('/')[1]
        otp = message.split('/')[2]
        result = check_otp(otp)
        print "Sent OTP check result to:-"+"/checkotp"+Username+"/"+Password
        client.publish("/checkotp"+Username+"/"+Password,result)
    elif("invalidate" in topic):
        Username = message.split('/')[0]
        Password = message.split('/')[1]
        delete_otp(Username,Password)
    else:
        #print "Incorrect details sent"
        print topic+":- "+ message

client = mqtt.Client()
client.connect("139.59.79.171")
client.subscribe("/register")
client.subscribe("/signup")
client.subscribe("/requestotp")
client.subscribe("/checkotp")
client.subscribe("/invalidate")
client.subscribe("test",qos = 2)
client.on_connect = on_connect
client.on_message = on_message_callback
client.loop_forever()
