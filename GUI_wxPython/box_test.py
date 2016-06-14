#! /usr/bin/env python
# encoding: utf-8

import wx

app = wx.App()  # アプリケーション初期化

frame = wx.Frame(None, wx.ID_ANY, u"テストフレーム", size=(570, 200))   # フレーム初期化
frame.Center()	# 中央へ表示

panel = wx.Panel(frame, wx.ID_ANY)  # パネル初期化
panel.SetBackgroundColour("#AFAFAF")

button_1 = wx.Button(panel, wx.ID_ANY, u"ボタン1", size=(80, 30)) # ボタン初期化
button_2 = wx.Button(panel, wx.ID_ANY, u"ボタン2", size=(80, 30))
button_3 = wx.Button(panel, wx.ID_ANY, u"ボタン3", size=(80, 30))
button_4 = wx.Button(panel, wx.ID_ANY, u"ボタン4", size=(80, 30))
button_5 = wx.Button(panel, wx.ID_ANY, u"ボタン5", size=(80, 30))
button_6 = wx.Button(panel, wx.ID_ANY, u"ボタン6", size=(80, 30))
button_7 = wx.Button(panel, wx.ID_ANY, u"ボタン7", size=(80, 30))

layout = wx.BoxSizer(wx.HORIZONTAL) # BoxSizerを横配置で初期化
layout.Add(button_1, flag=wx.GROW)    # BoxSizerへボタンを追加
layout.Add(button_2, flag=wx.SHAPED)
layout.Add(button_3, flag=wx.SHAPED | wx.ALIGN_TOP)
layout.Add(button_4, flag=wx.SHAPED | wx.ALIGN_BOTTOM)
layout.Add(button_5, flag=wx.SHAPED | wx.ALIGN_CENTER)
layout.Add(button_6, flag=wx.SHAPED | wx.ALIGN_LEFT)
layout.Add(button_7, flag=wx.SHAPED | wx.ALIGN_RIGHT)

panel.SetSizer(layout)  # パネルへBoxSizerをセット

frame.Show()
app.MainLoop()