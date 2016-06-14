#! /usr/bin/env python
# encoding: utf-8

import wx

app = wx.App()  # アプリケーション初期化

frame = wx.Frame(None, wx.ID_ANY, u"テストフレーム")   # フレーム初期化
frame.Show()    # フレーム表示 

app.MainLoop()