#! /usr/bin/env python
# encoding: utf-8

from Tkinter import *

root = Tk()
root.option_add("*font", ("FixedSys", 14))
root.title(u"式計算")

# 式を格納するオブジェクト
buff = StringVar()
buff.set("")

# Entryの生成
e = Entry(root, textvariable=buff)

# ListBoxの生成
lb = Listbox(root)

# Scrollbarの生成
sb1 = Scrollbar(root, orient="v", command=lb.yview)
sb2 = Scrollbar(root, orient="h", command=lb.xview)

# ListBoxの設定
lb.configure(yscrollcommand=sb1.set)    # リストボックスのY軸にスクロールバーを設置
lb.configure(xscrollcommand=sb2.set)    # X軸に

# Gridによる配置
e.grid(row=0, columnspan=2, sticky="ew")
lb.grid(row=1, column=0, sticky="nsew")
sb1.grid(row=1, column=1, sticky="ns")
sb2.grid(row=2, column=0, sticky="ew")

# 計算
def calc(event):
    expr = buff.get()
    lb.insert("end", expr)
    lb.see("end")
    val = eval(expr)
    buff.set(str(val))

# 取り出し
def get_expr(event):
    buff.set(lb.get("active"))
# 削除
def delete_expr(event):
    lb.delete("active")
    
# バインディング
e.bind("<Return>", calc)    # リターンキーが押されたらバインド
lb.bind("<Double-1>", get_expr) # ダブルクリックで取り出し
lb.bind("<Delete>", delete_expr)    # デリートキーで削除

root.mainloop()