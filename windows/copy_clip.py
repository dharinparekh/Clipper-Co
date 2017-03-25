import threading
import time

import paho.mqtt.client as mqtt
import pyperclip

print "Copy Clip Starts"

old_name = ""
old_pwd = ""
semaphore = 1
data = ""
pt = ""
Client = None

def on_connect(client, userdata, flags, rc):
    print("Connected with result code in copy clip "+str(rc))

def on_message_callback(client, userdata, msg):
    global semaphore, pt
    print msg.payload
    print "\n***********************************"
    print msg.topic+"  :  "+msg.payload
    print "***********************************"
    if msg.payload != pyperclip.paste() and msg.payload != pt and msg.payload != '':
        print "Updated from mqtt"
        pyperclip.copy(msg.payload)
        print "Current Clipboard Content: " + msg.payload
        semaphore = 0

def clip():
    global semaphore, clipboard, pt, old_name, old_pwd
    prevText = ''
    ctext = ''
    first_otp = True
    logout_flag = False
    while True:
        data = open('credentials.txt','r').read().split('\n')
        if len(data) == 2:
            Username, pwd = data
            if not first_otp:
                client.unsubscribe(old_name+"/"+old_pwd+"/cc")
                client.subscribe(Username+"/"+pwd+"/cc")
                first_otp = True
            if logout_flag:
                client.unsubscribe(old_name+"/"+old_pwd+"/cc")
                client.subscribe(Username+"/"+pwd+"/cc")
                
        elif len(data) == 4:
            try:
                Username, pwd = data[2], data[3]
                if first_otp:
                    client.unsubscribe(data[0]+"/"+data[1]+"/cc")
                    client.subscribe(Username+"/"+pwd+"/cc")
                    old_name = Username
                    old_pwd = pwd
                    first_otp = False
            except:
                continue
        else:
            logout_flag = True
            continue
        old_name = Username
        old_pwd = pwd
        ctext = pyperclip.paste()
        if ctext == prevText:
            pass
        elif ctext != '' and prevText != '':
            print "\n\nT: " + ctext + " S: " + str(semaphore) + " PT: " + prevText
            #print "Text Copied"
            if semaphore == 1 and ctext != '':
                # Not changed by mqtt
                print "Published"
                client.publish(Username+"/"+pwd+"/cc", ctext)
                pt = ctext
            semaphore = 1
        prevText = ctext

def on_disconnect(a=1, b=2, c=3):
    reconnect()

def main():
    global client
    client = mqtt.Client()
    client.connect("139.59.79.171")
    client.on_connect = on_connect
    client.on_message = on_message_callback
    client.on_disconnect = on_disconnect
    data = open('credentials.txt','r').read().split('\n')
    Username,pwd = data
    client.subscribe(Username+"/"+pwd+"/cc")
    print "Clip() Thread Running..."
    th1 = threading.Thread(target=clip)
    th1.start()
    print "Looping forever.."
    client.loop_forever()
