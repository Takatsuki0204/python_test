#! /usr/bin/env python
# encoding: utf-8

from Tkinter import *

root = Tk()
root.option_add("*font", ("FixedSys", 14))

column_data = (0, 0, 1, 1)
row_data =(0, 1, 0, 1)

for x in xrange(4):
    b = Button(root, text="button %d" % x)
    b.grid(column=column_data[x], row=row_data[x], sticky="news")

root.grid_rowconfigure(0, weight = 1)
root.grid_rowconfigure(1, weight = 2)

root.mainloop()