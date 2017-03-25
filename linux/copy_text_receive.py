import threading
import time
import sys
import paho.mqtt.client as mqtt
import pyperclip
osVersion = sys.platform
platform = ''
specialFlag = False
saveControl = ''
saveKey = ''
Username = ''
password = ''
toPublish = True
counter = 0
if 'linux' in osVersion:
    platform = 'linux'
elif 'win' in osVersion:
    platform = 'windows'
elif 'posix' in osVersion:
    platform = 'mac'

if platform== 'mac':
    print 'Not supported yet'
    exit(0)
elif platform == 'linux':
    import pyxhook as ph
    import pyautogui as pag

specialKeys = ['Control_L','Alt_L','Shift_L','Control_R','Alt_R','Shift_R']
def on_connect(client, userdata, flags, rc):
    pass

def on_message_callback(client, userdata, msg):
    # print msg.payload
    toPublish = False
    if "Special" in msg.payload:
        message = msg.payload.split()
        controlKey = message[2]
        plainKey = message[1]
        if "Control" in controlKey:
            controlKey = 'ctrl'
        elif "Shift" in controlKey:
            controlKey = 'shift'
        elif "Alt" in controlKey:
            controlKey = 'alt'
        print "hotkey",controlKey,plainKey
        pag.hotkey(controlKey,plainKey)
    else:
        keyToPrint = ''
        print "Got this "+str(msg.payload)
        msg.payload = msg.payload.lower()
        if msg.payload == 'grave':
            keyToPrint = '`'
        elif msg.payload == 'minus':
            keyToPrint = '-'
        elif msg.payload == 'equal':
            keyToPrint = '='
        elif msg.payload == 'backslash':
            keyToPrint = '\\'
        elif msg.payload == 'apostrophe':
            keyToPrint = "'"
        elif msg.payload == 'semicolon':
            keyToPrint = ';'
        elif msg.payload == 'comma':
            keyToPrint = ','
        elif msg.payload == 'period':
            keyToPrint = '.'
        elif msg.payload == 'slash':
            keyToPrint = '/'
        elif msg.payload == 'next':
            keyToPrint = 'pagedown'
        elif msg.payload == 'page_up':
            keyToPrint = 'pageup'
        elif msg.payload == 'escape':
            keyToPrint = 'esc'
        elif msg.payload == 'super_l':
            keyToPrint = 'winleft'
        elif msg.payload == 'caps_lock':
            keyToPrint = 'capslock'
        elif msg.payload == 'question':
            keyToPrint = '?'
        elif msg.payload == 'greater':
            keyToPrint = '>'
        elif msg.payload == 'less':
            keyToPrint = '<'
        elif msg.payload == 'quotedbl':
            keyToPrint = '"'
        elif msg.payload == 'colon':
            keyToPrint = ':'
        elif msg.payload == 'bar':
            keyToPrint = '|'
        elif msg.payload == 'braceright':
            keyToPrint = '}'
        elif msg.payload == 'bracketright':
            keyToPrint = ']'
        elif msg.payload == 'bracketleft':
            keyToPrint = '['
        elif msg.payload == 'braceleft':
            keyToPrint = '{'
        elif msg.payload == 'plus':
            keyToPrint = '+'
        elif msg.payload == 'underscore':
            keyToPrint = '_'
        elif msg.payload == 'parenright':
            keyToPrint = ')'
        elif msg.payload == 'parenleft':
            keyToPrint = '('
        elif msg.payload == 'asterisk':
            keyToPrint = '*'
        elif msg.payload == 'ampersand':
            keyToPrint = '&'
        elif msg.payload == 'asciicircum':
            keyToPrint = '^'
        elif msg.payload == 'percent':
            keyToPrint = '%'
        elif msg.payload == 'dollar':
            keyToPrint = '$'
        elif msg.payload == 'numbersign':
            keyToPrint = '#'
        elif msg.payload == 'at':
            keyToPrint = '@'
        elif msg.payload == 'exclam':
            keyToPrint = '!'
        elif msg.payload == 'asciitilde':
            keyToPrint = '~'
        else :
            keyToPrint = msg.payload
        print keyToPrint
        pag.press(keyToPrint)

# def kbhit(event):
#     global specialKeys,specialFlag,saveControl,saveKey,Username,password,toPublish,counter
#     counter+=1
#     if specialFlag == True:
#         saveKey = event.Key
#         if saveControl!='' and saveKey!='':
#             print 'Special '+saveKey+' '+saveControl
#             specialFlag = False
#     else:
#         if(event.Key in specialKeys):
#             specialFlag = True
#             saveControl = event.Key
#         else:
#             if(toPublish):
#                 print "hello"
#                 client.publish("test", event.Key)
#             else:
#                 toPublish = True
#
#mqtt setup
client = mqtt.Client()
client.connect("139.59.79.171")
client.on_connect = on_connect
client.on_message = on_message_callback
data = open('credentials.txt','r').read().split('\n')
Username,pwd = data[:2]
client.subscribe("test",qos = 1)
client.loop_forever()
