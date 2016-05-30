#! /usr/bin/env python
# encoding: utf-8

from Tkinter import *

root = Tk()
root.option_add("*font", ("FixedSys", 14))

# expand = boolean : ウインドウに余白が生じた時、Trueであれば余白をウィジェットに割り当てる
Button(root, text="button 0").pack(expand=True, fill=BOTH)
Button(root, text="button 1").pack(expand=True, fill=BOTH)

root.mainloop()