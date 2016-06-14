#! /usr/bin/env python
# encoding: utf-8

import wx

app = wx.App()  # アプリケーション初期化

frame = wx.Frame(None, wx.ID_ANY, u"テストフレーム", size=(300, 300), pos=(0, 0))   # フレーム初期化
#frame.Center() # 中央へ表示

frame.CreateStatusBar()
frame.SetStatusText("wxPython-test")
frame.Show()    # フレーム表示 

app.MainLoop()