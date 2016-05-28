#! /usr/bin/env python
# encoding: utf-8

from Tkinter import *

root = Tk()

buff = StringVar()
buff.set("")

label = Label(root, textvariable=buff)
label.pack(anchor="w")  # ラベルの表示位置(w:west)

# コールバック関数の生成
def make_cmd(n):
    return lambda : buff.set("button %d pressed" % n)

# ボタンの生成
for x in xrange(4):
    button = Button(root, text="Button %d" % x, command=make_cmd(x))
    button.pack(fill="both", side="left")   # side:並び順

root.mainloop()