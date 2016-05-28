#! /usr/bin/env python
# encoding: utf-8

from Tkinter import *

root = Tk()
root.option_add("*font", ("FixedSys", 14))

# 式を格納するオブジェクト
buff = StringVar()
buff.set("")

# 計算
def calc(event):
    if buff.get():
        value = eval(buff.get())    # 文字列の式評価(計算)
        buff.set(str(value))

# エントリー
e = Entry(root, textvariable=buff)
e.pack()
e.focus_set()   # フォーカスをエントリー(一行入力ボックス)に

# バインディング
e.bind("<Return>", calc)    # リターンキーが押されたらバインド

root.mainloop()