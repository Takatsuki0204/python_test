#! /usr/bin/env python
# encoding: utf-8

from Tkinter import *
from time import *

root = Tk()
root.option_add("*font", ("FixedSys", 14))
root.title("Timer")

buff = StringVar()
buff.set("")
fn = IntVar()
fn.set(0)
fs = IntVar()
fs.set(0)

def changefont():
    if fn.get() == 0:
        lb.configure(font=("FixedSys", 20))
    elif fn.get() == 1:
        lb.configure(font=("Arial", 50))
    elif fn.get() == 2:
        lb.configure(font=("Times", 50))

def show_time():
    buff.set(strftime("%H:%M:%S"))
    root.after(1000, show_time)

lb = Label(textvariable=buff)
lb.pack()

mbar = Menu(root)
root.configure(menu=mbar)

font = Menu(mbar, tearoff=False)
mbar.add_cascade(label="Font", underline=0, menu=font)

font.add_radiobutton(label="FixedSys", variable=fn,
                     value=0, command=changefont)
font.add_radiobutton(label="Arial", variable=fn,
                     value=1, command=changefont)
font.add_radiobutton(label="Timer", variable=fn,
                     value=2, command=changefont)

show_time()
root.mainloop()