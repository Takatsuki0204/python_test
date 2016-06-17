#! /usr/bin/pyton
# encoding: utf-8

import wx

def listbox_select(event):
    obj = event.GetEventObject()
    frame.SetStatusText("listbox: " + obj.GetStringSelection())

app = wx.App()
frame = wx.Frame(None, wx.ID_ANY, u"テストフレーム", size=(300, 200))
frame.CreateStatusBar()
frame.Center()

panel = wx.Panel(frame, wx.ID_ANY)
panel.SetBackgroundColour("#AFAFAF")

array = ("list1", "list2", "list3", "list4", "list5")
listbox = wx.ListBox(panel, wx.ID_ANY, choices=array, style=wx.LB_SINGLE | wx.LB_HSCROLL)   # 収まりきらなかった場合横スクロール追加
# listbox = wx.ListBox(panel, wx.ID_ANY, choices=array, style=wx.LB_MALTIPLE | wx.LB_ALWAYS_SB) # 複数選択1、常時縦スクロール追加
# listbox = wx.ListBox(panel, wx.ID_ANY, choices=array, style=wx.LB_EXTENDED | wx.LB_NEEDED_SB) # 複数選択2、収まりきらなかった場合縦スクロール追加

listbox.Append("list6")

listbox.SetSelection(2)
listbox.SetStringSelection("list5")
print listbox.GetSelection()
print listbox.GetStringSelection()

listbox.Bind(wx.EVT_LISTBOX, listbox_select)

layout = wx.GridSizer(1, 1)
layout.Add(listbox, flag=wx.GROW | wx.ALL, border=10)

panel.SetSizer(layout)

frame.Show()
app.MainLoop()