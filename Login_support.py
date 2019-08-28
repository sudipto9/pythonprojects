
import sys
from SecondPage_support import *
import SecondPage

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def Login_Lclick():
    print('Login_support.Login_Lclick')
    sys.stdout.flush()

def callsecondpage():
    destroy_window()
    SecondPage.vp_start_gui()
    sys.stdout.flush()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import Login
    Login.vp_start_gui()




