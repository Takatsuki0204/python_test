#! /usr/bin/env python
# encoding: utf-8

import wx

app = wx.App()  # アプリケーション初期化

frame = wx.Frame(None, wx.ID_ANY, u"テストフレーム",
                 size=(300, 300), pos=(0, 0))   # フレーム初期化
# frame.Center() # 中央へ表示
frame.SetBackgroundColour("#000000")    # フレームの背景色を黒に

frame.CreateStatusBar()  # ステータスバー表示
frame.SetStatusText("wxPython-test")    # バーへのテキスト追加

icon = wx.Icon("RoBoHoN.ico", wx.BITMAP_TYPE_ICO)   # アイコン追加
frame.SetIcon(icon)

r_panel = wx.Panel(frame, wx.ID_ANY, pos=(0, 0), size=(80, 230))    # 赤パネル初期化
r_panel.SetBackgroundColour("#FF0000")  # HTMLカラーコードで指定

g_panel = wx.Panel(frame, wx.ID_ANY, pos=(80, 0), size=(80, 230))   # 緑パネル初期化
g_panel.SetBackgroundColour("#00FF00")

b_panel = wx.Panel(frame, wx.ID_ANY, pos=(160, 0), size=(80, 230))  # 青パネル初期化
b_panel.SetBackgroundColour("#0000FF")

frame.Show()    # フレーム表示

app.MainLoop()
