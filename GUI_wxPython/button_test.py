#! /usr/bin/python
# encoding: utf-8

import wx

app = wx.App()
frame = wx.Frame(None, wx.ID_ANY, u"テストフレーム", size=(300, 200))

panel = wx.Panel(frame, wx.ID_ANY)
panel.SetBackgroundColour("#AFAFAF")

button_1 = wx.Button(panel, wx.ID_ANY, u"ボタン1")
button_2 = wx.Button(panel, wx.ID_ANY, u"ボタン2", size=(50, 50))
button_3 = wx.Button(panel, wx.ID_ANY, u"ボタン3")

# button_3.SetLabel(u"Button_3")  # ラベル変更
# button_3.SetSize((50, 50))      # サイズ変更
# button_3.SetMinSize((50, 50))
# button_3.SetMaxSize((50, 50))

font = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTWEIGHT_NORMAL,
               wx.FONTWEIGHT_NORMAL)   # フォント設定
button_3.SetFont(font)  # フォントセット

button_3.SetForegroundColour("#FF0000") # フォントカラー変更
button_3.SetBackgroundColour("#00FF00") # ボタンバックカラー変更

button_3.Disable()    # 無効化
# button_3.Enable()     # 有効化
# button_3.Hide()     # 非表示
# button_3.Show()     # 表示

button_1.SetToolTipString(u"ボタンです") # ツールチップ設定

layout = wx.BoxSizer(wx.VERTICAL)
layout.Add(button_1)
layout.Add(button_2)
layout.Add(button_3)

panel.SetSizer(layout)

frame.Show()
app.MainLoop()
