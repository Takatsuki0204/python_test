#! /usr/bin/env python
# encoding: utf-8

from Tkinter import *

root = Tk()
root.title("Main")
root.option_add("*font", "FixedSys", 14)
sub_win = None

# message view
def message_window():
    global sub_win
    if sub_win is None or not sub_win.winfo_exists():
        sub_win = Toplevel()
        sub_win.title = "About"
        Message(sub_win, text=u"message のサンプルプログラムです").pack()

# menu settings
m = Menu(root)
root.configure(menu=m)
m.add_command(label="About", under=0, command=message_window)

# label settings
Label(root, text=u"メニュー About を選んでください").pack()

root.mainloop()