#! /usr/bin/env python
# encoding: utf-8

from Tkinter import *
from time import *

root = Tk()
root.option_add("*font", ("FixedSys", 14))

buff = StringVar()
buff.set("")

Label(textvariable=buff).pack()

def show_time():
    buff.set(strftime("%H:%M:%S"))
    root.after(1000, show_time)     # after:指定された時間(ms)だけ待ち、指定したコマンドを実行(タイマー機能)

show_time()
root.mainloop()