#! /usr/bin/python
# encoding: utf-8

import wx

app = wx.App()  # アプリケーション初期化
frame = wx.Frame(None, wx.ID_ANY, u"テストフレーム", size=(300, 300))  # フレーム初期化

panel = wx.Panel(frame, wx.ID_ANY)  # パネル初期化
panel.SetBackgroundColour("#AFAFAF")

button_1 = wx.Button(panel, wx.ID_ANY, "1")
button_2 = wx.Button(panel, wx.ID_ANY, "2")
button_3 = wx.Button(panel, wx.ID_ANY, "3")
button_4 = wx.Button(panel, wx.ID_ANY, "4")

layout = wx.GridSizer(2, 2)  # GridSizerを2行2列で初期化
layout.Add(button_1, flag=wx.EXPAND | wx.TOP, border=10)
layout.Add(button_2, flag=wx.EXPAND | wx.LEFT, border=10)
layout.Add(button_3, flag=wx.EXPAND | wx.RIGHT, border=10)
# layout.Add(button_4, flag=wx.EXPAND | wx.BOTTOM, border=10)
layout.Add(button_4, flag=wx.EXPAND | wx.ALL, border=10)

panel.SetSizer(layout)  # パネルへGridSizerをセット

frame.Show()
app.MainLoop()
