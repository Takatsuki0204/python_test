#! /usr/bin/python
# encoding: utf-8

import wx


def select_RB(event):
    obj = event.GetEventObject()
    frame.SetStatusText("Selected! " + obj.GetStringSelection())

app = wx.App()
frame = wx.Frame(None, wx.ID_ANY, u"テストフレーム", size=(300, 250))
frame.CreateStatusBar()

panel = wx.Panel(frame, wx.ID_ANY)

btn_array = ("RB1", "RB2", "RB3", "RB4", "RB5")
radio_box = wx.RadioBox(panel, wx.ID_ANY, "RadioBox_test",
                        choices=btn_array, style=wx.RA_HORIZONTAL)

btn_array2 = ("RB1", "RB2", "RB3", "RB4", "RB5", "RB6", "RB7", "RB8", "RB9")
# 縦配置で、折り返して3つずつ配置(majorDimension=3)
radio_box2 = wx.RadioBox(panel, wx.ID_ANY, "RadioBox_test2",
                         choices=btn_array2, majorDimension=3, style=wx.RA_VERTICAL)

# タプル指定して名前変更
radio_box2.SetItemLabel(1, u"ラジオボックス2")
radio_box2.SetString(2, u"ラジオボックス3")

radio_box2.EnableItem(5, False)  # タプル指定して有効無効 True:有効 False:無効

radio_box.SetItemToolTip(1, u"選択してください。")   # ツールチップ設定

radio_box.Bind(wx.EVT_RADIOBOX, select_RB)  # イベント追加

radio_box.SetSelection(0)   # 選択状態の設定
radio_box.SetStringSelection("RB2")

print radio_box.GetSelection()  # 選択状態の取得(タプル番号)
print radio_box2.GetStringSelection()   # 文字列

layout = wx.BoxSizer(wx.VERTICAL)
layout.Add(radio_box)
layout.Add(radio_box2)

panel.SetSizer(layout)

frame.Show()
app.MainLoop()
