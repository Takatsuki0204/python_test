#! /usr/bin/env python
# encoding: utf-8

from Tkinter import *

root = Tk()
root.option_add("*font", ("FixedSys", 14))
root.title("sub window")

def message_window():
    sub_win = Toplevel()
    Message(sub_win, text="message のサンプルプログラムです").pack()

# menuの設定
m = Menu(root)
root.configure(menu=m)
m.add_command(label="About", under=0, command=message_window)

# ラベルの設定
Label(root, text="メニュー About を選択してね").pack()

root.mainloop()