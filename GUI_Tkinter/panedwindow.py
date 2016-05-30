#! /usr/bin/env python
# encoding: utf-8

from Tkinter import *

root = Tk()
root.option_add("*font", ("FixedSys", 14))

# 横2分割
## ペインドウィンドウの生成
#pw = PanedWindow(root, sashwidth=4)
#pw.pack(expand=True, fill=BOTH)

## label
#a = Label(pw, text="panedwindow\ntest1", bg="white")
#b = Label(pw, text="panedwindow\ntest2", bg="yellow")

## ペインドウィンドウに追加
#pw.add(a)
#pw.add(b)

# 縦3分割
# ペインドウィンドウの生成
pw = PanedWindow(root, orient = 'vertical', sashwidth = 4)
pw.pack(expand = True, fill = BOTH)

# ラベルの生成
a = Label(pw, text = 'panedwindow\ntest1', bg = 'white')
b = Label(pw, text = 'panedwindow\ntest2', bg = 'yellow')
c = Label(pw, text = 'panedwindow\ntest3', bg = 'cyan')

# ペインドウィンドウに配置
pw.add(a)
pw.add(b)
pw.add(c)

root.mainloop()