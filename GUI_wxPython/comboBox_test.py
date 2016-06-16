#! /usr/bin/python
# encoding: utf-8

import wx


def cb_event(event):
    obj = event.GetEventObject()
    frame.SetStatusText("combobox_1: " + obj.GetStringSelection())


def text_event(event):
    obj = event.GetEventObject()
    frame.SetStatusText("combobox_2: " + obj.GetValue())

app = wx.App()
frame = wx.Frame(None, wx.ID_ANY, u"テストフレーム", size=(300, 500))
frame.CreateStatusBar()

panel = wx.Panel(frame, wx.ID_ANY)
panel.SetBackgroundColour("#AFAFAF")

com_array = ("COM1", "COM2", "COM3", "COM4", "COM5")
combobox_1 = wx.ComboBox(panel, wx.ID_ANY, u"選択してください。",
                         choices=com_array, style=wx.CB_SIMPLE)   # シンプル型(初めから選択肢が見える)

combobox_2 = wx.ComboBox(panel, wx.ID_ANY, u"選択してください。",
                         choices=com_array, style=wx.CB_DROPDOWN)   # ドロップダウン型(選択肢が見えない)

# ソートして表示も可能
combobox_3 = wx.ComboBox(panel, wx.ID_ANY, u"選択してください。",
                         choices=com_array, style=wx.CB_READONLY | wx.CB_SORT)   # リードオンリー型(ユーザ入力不可)

combobox_1.Append("COM10")  # 要素の追加
combobox_1.Delete(1)    # 1要素削除
# combobox_2.Clear()      # 全要素削除

for i in combobox_3.GetItems():  # アイテム取得
    print i
print combobox_3.GetCount()  # アイテム数取得

combobox_3.SetSelection(3)  # 選択状態の設定(タプル)
combobox_2.SetStringSelection("COM2")   # 選択状態の設定(アイテム名)
print combobox_2.GetSelection()  # 選択状態の取得(タプル)
print combobox_3.GetStringSelection()   # 選択状態の取得(アイテム名)

combobox_1.Bind(wx.EVT_COMBOBOX, cb_event)
combobox_2.Bind(wx.EVT_TEXT, text_event)

layout = wx.BoxSizer(wx.VERTICAL)
layout.Add(combobox_1, flag=wx.GROW)
layout.Add(combobox_2, flag=wx.GROW)
layout.Add(combobox_3, flag=wx.GROW)

panel.SetSizer(layout)

frame.Show()
app.MainLoop()
