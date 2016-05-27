#! /usr/bin/env python
# encoding: utf-8

from Tkinter import *

root = Tk()
button = Button(root, text="Python/Tkinter", command=lambda:sys.exit(1))    # ボタンのオブジェクト生成
label = Label(root, text="Python/label")
rb = Radiobutton(root, text="python")
button.pack()   # 配置
label.pack()
rb.pack()
root.mainloop() # イベントのループ