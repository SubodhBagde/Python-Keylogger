from pynput.mouse import Listener

def position(x,y):
    print("Current position of mouse {0}".format(x,y))

with Listener(on_move=position) as l:
    l.join()
