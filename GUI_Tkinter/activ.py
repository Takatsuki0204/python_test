#! /usr/bin/env python
# encoding: utf-8

from Tkinter import *

root = Tk()
root.option_add("*font", ("FixedSys", 14))

var = StringVar()
var.set("nomal")

# button
b = Button(root, text="button", activeforeground="green", disabledforeground="red")
b.pack(fill=X)

# change state
def change_state(): b.configure(state=var.get())

# radiobutton settings
for x in ("nomal", "active", "disabled"):
    Radiobutton(root, text=x, value=x, variable=var, command=change_state).pack(anchor=W)

root.mainloop()