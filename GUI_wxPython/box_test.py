#! /usr/bin/env python
# encoding: utf-8

import wx

app = wx.App()  # アプリケーション初期化

frame = wx.Frame(None, wx.ID_ANY, u"テストフレーム", size=(400, 200))   # フレーム初期化
frame.Center()	# 中央へ表示

panel = wx.Panel(frame, wx.ID_ANY)  # パネル初期化
panel.SetBackgroundColour("#AFAFAF")

button_1 = wx.Button(panel, wx.ID_ANY, u"ボタン1") # ボタン初期化
button_2 = wx.Button(panel, wx.ID_ANY, u"ボタン2")
button_3 = wx.Button(panel, wx.ID_ANY, u"ボタン3")

layout = wx.BoxSizer(wx.HORIZONTAL) # BoxSizerを横配置で初期化
layout.Add(button_1)    # BoxSizerへボタンを追加
layout.Add(button_2)
layout.Add(button_3)

panel.SetSizer(layout)  # パネルへBoxSizerをセット

frame.Show()
app.MainLoop()