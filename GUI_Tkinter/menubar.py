#! /usr/bin/env python
# encoding: utf-8

from Tkinter import *
import sys

root = Tk()
root.option_add("*font", ("FixedSys", 14))

# ダミー
def start(): pass

# variable 用のオブジェクト
action = IntVar()
action.set(0)
level = IntVar()
level.set(1)

# メニューバーの生成
menubar = Menu(root)
root.configure(menu = menubar)

# メニューの設定
games = Menu(menubar, tearoff = False)
levels = Menu(menubar, tearoff = False)
opt = Menu(menubar, tearoff = False)
menubar.add_cascade(label="Games", underline = 0, menu=games)
menubar.add_cascade(label="Level", underline = 0, menu=levels)
menubar.add_cascade(label="Option", underline = 0, menu=opt)

# Games
games.add_command(label = "Start", under = 0, command = start)
games.add_separator()
games.add_radiobutton(label = "first", variable = action, value = 0)
games.add_radiobutton(label = "second", variable = action, value = 1)
games.add_separator()
games.add_command(label = "exit", under = 0, command = sys.exit)

# Labels
levels.add_radiobutton(label = 'Level 1', variable = level, value = 1)
levels.add_radiobutton(label = 'Level 2', variable = level, value = 2)
levels.add_radiobutton(label = 'Level 3', variable = level, value = 3)

# ラベル
Label(root, text = "***** Menu Test *****").pack()

root.mainloop()