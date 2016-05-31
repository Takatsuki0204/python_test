#! /usr/bin/env python
# encoding: utf-8

from Tkinter import *
from time import *

root = Tk()
root.option_add("*font", ("FixedSys", 14))
root.title("Timer")

buff = StringVar()
buff.set("")
action = IntVar()
action.set(0)

lb = Label(textvariable=buff)
lb.pack()

def changefont():
    if action.get() == 0:
        lb.configure(font=("FixedSys", 20))
    elif action.get() == 1:
        lb.configure(font=("Arial", 20))
    elif action.get() == 2:
        lb.configure(font=("Times", 20))

mbar = Menu(root)
root.configure(menu=mbar)

font = Menu(mbar, tearoff=False)
mbar.add_cascade(label="Font", underline=0, menu=font)
font.add_radiobutton(label="FixedSys", variable=action, value=0, command=changefont)
font.add_radiobutton(label="Arial", variable=action, value=1, command=changefont)
font.add_radiobutton(label="Timer", variable=action, value=2, command=changefont)

def show_time():
    buff.set(strftime("%H:%M:%S"))
    root.after(1000, show_time)     # after:指定された時間(ms)だけ待ち、指定したコマンドを実行(タイマー機能)

show_time()
root.mainloop()