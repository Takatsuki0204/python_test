#! /usr/bin/env python
# encoding: utf-8

from Tkinter import *

root = Tk()
root.option_add("*font", ("FixedSys", 14))
root.title(u"Check and Radio")

opt1 = BooleanVar()
opt1.set(True)
opt2 = BooleanVar()
opt2.set(False)
opt3 = BooleanVar()
opt3.set(True)

action = IntVar()
action.set(1)

Label(text="Check Button").pack()
Checkbutton(text="option 1", variable=opt1).pack()
Checkbutton(text="option 2", variable=opt2).pack()
Checkbutton(text="option 3", variable=opt3).pack()

Label(text="Radio Button").pack()
Radiobutton(text="action 1", variable=action, value=0).pack()
Radiobutton(text="action 2", variable=action, value=1).pack()
Radiobutton(text="action 3", variable=action, value=2).pack()

root.mainloop()