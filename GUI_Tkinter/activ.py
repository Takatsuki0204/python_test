#! /usr/bin/env python
# encoding: utf-8

from Tkinter import *

root = Tk()
root.option_add("*font", ("FixedSys", 14))

var = StringVar()
var.set("nomal")

def dummy(): pass

# menu
m0 = Menu(root)
root.configure(menu=m0)

m1 = Menu(m0, tearoff=False)
m0.add_cascade(label="Menu", under=0, menu=m1)
m1.add_command(label="Menu1", command=dummy())
m1.add_command(label="Menu2", command=dummy())
m1.add_command(label="Menu3", command=dummy())

# change state
def change_state():
    m1.entryconfigure("Menu1", state=var.get())

# radiobutton settings
for x in ("normal", "active", "disabled"):
    Radiobutton(root, text=x, value=x, variable=var, command=change_state).pack(anchor=W)

root.mainloop()