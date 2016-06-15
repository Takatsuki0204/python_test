#! /usr/bin/python
# encoding: utf-8

import wx

app = wx.App()
frame = wx.Frame(None, wx.ID_ANY, u"テストフレーム", size=(300, 300))

panel = wx.Panel(frame, wx.ID_ANY)
panel.SetBackgroundColour("#AFAFAF")

button_1 = wx.Button(panel, wx.ID_ANY, "1")
button_2 = wx.Button(panel, wx.ID_ANY, "2")
button_3 = wx.Button(panel, wx.ID_ANY, "3")
button_4 = wx.Button(panel, wx.ID_ANY, "4")
button_5 = wx.Button(panel, wx.ID_ANY, "5")
button_6 = wx.Button(panel, wx.ID_ANY, "6")

layout = wx.FlexGridSizer(3, 2)
layout.Add(button_1, flag=wx.GROW)
layout.Add(button_2, flag=wx.GROW)
layout.Add(button_3, flag=wx.GROW)
layout.Add(button_4, flag=wx.GROW)
layout.Add(button_5, flag=wx.GROW)
layout.Add(button_6, flag=wx.GROW)
layout.AddGrowableRow(0)    # サイズ変更したい行を指定
layout.AddGrowableCol(1)    # 列を指定

panel.SetSizer(layout)

frame.Show()
app.MainLoop()