from pynput.mouse import Controller
from pynput.keyboard import Controller
# mouse.position = (left to right(in px), top to bottom(in px)
# from top left of the screen you can imagine the top left to be (0,0)
def controlMouse():
    mouse =  Controller()
    mouse.position = (5,5)

def contolKeyboard():
    keyboard =  Controller()
    keyboard.type("hello")

contolKeyboard()
# controlling the mouse
# listening the mouse
# controlling the keyboard
# listening the keyboard

