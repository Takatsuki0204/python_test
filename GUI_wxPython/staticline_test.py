#! /usr/bin/python
# encoding: utf-8

import wx

app = wx.App()
frame = wx.Frame(None, wx.ID_ANY, u"テストフレーム", size=(300, 200))

panel = wx.Panel(frame, wx.ID_ANY)
panel.SetBackgroundColour("#AFAFAF")

button_1 = wx.Button(panel, wx.ID_ANY, "1")
button_2 = wx.Button(panel, wx.ID_ANY, "2")
button_3 = wx.Button(panel, wx.ID_ANY, "3")
button_4 = wx.Button(panel, wx.ID_ANY, "4")

layout = wx.BoxSizer(wx.VERTICAL)
layout.Add(button_1)
layout.Add(button_2)
layout.Add(wx.StaticLine(panel), flag=wx.GROW)  # ライン
layout.Add(button_3)
layout.Add(button_4)

panel.SetSizer(layout)

frame.Show()
app.MainLoop()
