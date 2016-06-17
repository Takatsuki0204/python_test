#! /usr/bin/env python
# encoding: utf-8

import wx

def slider_value_change(event):
    obj = event.GetEventObject()
    frame.SetStatusText("Slider value is " + str(obj.GetValue()))

app = wx.App()  # アプリケーション初期化

frame = wx.Frame(None, wx.ID_ANY, u"テストフレーム", size=(300, 300))   # フレーム初期化
frame.CreateStatusBar()
frame.Center()  # 中央へ表示

panel = wx.Panel(frame, wx.ID_ANY)  # パネル初期化
panel.SetBackgroundColour("#AFAFAF")

slider = wx.Slider(panel, style=wx.SL_LABELS | wx.SL_AUTOTICKS)   # 最小、最大、現在値の表示、メモリ追加
# slider = wx.Slider(panel, style=wx.SL_VERTICAL)   # 縦表示

slider.SetTickFreq(10)  # 追加メモリ幅指定

slider.SetMin(100)  # 最小値、最大値の設定
slider.SetMax(500)

slider.SetValue(150)
print slider.GetValue()

slider.Bind(wx.EVT_SLIDER, slider_value_change)

layout = wx.BoxSizer(wx.VERTICAL)
layout.Add(slider, flag=wx.GROW)

panel.SetSizer(layout)

frame.Show()
app.MainLoop()
