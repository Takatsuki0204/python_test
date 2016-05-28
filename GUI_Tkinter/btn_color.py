#! /usr/bin/env python
# encoding: utf-8

from Tkinter import *

root = Tk()

# スケールの値を格納
red = IntVar()
red.set(0)
blue = IntVar()
blue.set(0)
green = IntVar()
green.set(0)

# ボタンの背景色を変更
def change_color(n):
    color = "#%02x%02x%02x" % (red.get(), green.get(), blue.get())
    button.configure(bg = color)    # 後から変更する場合は.configure

# ボタン
button = Button(root, text="button", bg="#000")
button.pack(fill="both")

# スケール
s1 = Scale(root, label="RED", orient="h", from_=0, to=255, variable=red, command=change_color)
s2 = Scale(root, label="BLUE", orient="h", from_=0, to=255, variable=blue, command=change_color)
s3 = Scale(root, label="GREEN", orient="h", from_=0, to=255, variable=green, command=change_color)

# ウィジェットの配置
s1.pack(fill="both")
s2.pack(fill="both")
s3.pack(fill="both")

root.mainloop()