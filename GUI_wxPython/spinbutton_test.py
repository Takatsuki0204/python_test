#! /usr/bin/env python
# encoding: utf-8

import wx

def spinbutton_value_change(event):
    obj = event.GetEventObject()
    frame.SetStatusText("SpinButton value is " + str(obj.GetValue()))

app = wx.App()  # アプリケーション初期化
frame = wx.Frame(None, wx.ID_ANY, u"テストフレーム", size=(300, 300))   # フレーム初期化
frame.CreateStatusBar()
frame.Center()  # 中央へ表示

panel = wx.Panel(frame, wx.ID_ANY)  # パネル初期化
panel.SetBackgroundColour("#AFAFAF")

spin_button = wx.SpinButton(panel, style=wx.SP_HORIZONTAL)   # 横表示
# spin_button = wx.SpinButton(panel, style=wx.SP_VERTICAL)   # 縦表示

spin_button.SetMin(100)  # 最小値、最大値の設定
spin_button.SetMax(500)

spin_button.SetValue(150)
print spin_button.GetValue()

spin_button.Bind(wx.EVT_SPIN, spinbutton_value_change)

layout = wx.GridSizer(3, 1)
layout.Add(spin_button, flag=wx.GROW | wx.ALL, border=10)

panel.SetSizer(layout)

frame.Show()
app.MainLoop()
