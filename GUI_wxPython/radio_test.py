#! /usr/bin/python
# encoding: utf-8

import wx


def select_rb_1(event):
    frame.SetStatusText("Selected! Radiobutton_1")


def select_rb_3(event):
    frame.SetStatusText("Selected! Radiobutton_3")


def select_rb(event):
    if event.GetId() == 4444:
        frame.SetStatusText("Selected! Radiobutton_4")
    elif event.GetId() == 5555:
        frame.SetStatusText("Selected! Radiobutton_5")

app = wx.App()
frame = wx.Frame(None, wx.ID_ANY, u"テストフレーム", size=(300, 200))
frame.CreateStatusBar()

panel = wx.Panel(frame, wx.ID_ANY)
panel.SetBackgroundColour("#AFAFAF")

# スタイルの指定で次のグループ指定があるまでは同一グループとみなされる
rb_1 = wx.RadioButton(panel, wx.ID_ANY, u"ラジオボタン1", style=wx.RB_GROUP)
rb_2 = wx.RadioButton(panel, wx.ID_ANY, u"ラジオボタン2")
rb_3 = wx.RadioButton(panel, wx.ID_ANY, u"ラジオボタン3")
rb_4 = wx.RadioButton(panel, 4444, u"ラジオボタン4", style=wx.RB_GROUP)
rb_5 = wx.RadioButton(panel, 5555, u"ラジオボタン5")

rb_1.Bind(wx.EVT_RADIOBUTTON, select_rb_1)
rb_3.Bind(wx.EVT_RADIOBUTTON, select_rb_3)
frame.Bind(wx.EVT_RADIOBUTTON, select_rb, rb_4)
frame.Bind(wx.EVT_RADIOBUTTON, select_rb, rb_5)

rb_3.SetLabel("RadioButton3")

rb_3.SetToolTipString(u"選択してください。")

rb_2.Disable()
# rb_2.Enable()

rb_1.SetValue(False)
rb_2.SetValue(True)
rb_3.SetValue(False)

print rb_1.GetValue()
print rb_2.GetValue()
print rb_3.GetValue()
print rb_4.GetValue()
print rb_5.GetValue()

layout = wx.BoxSizer(wx.VERTICAL)
layout.Add(rb_1, flag=wx.GROW)
layout.Add(rb_2, flag=wx.GROW)
layout.Add(rb_3, flag=wx.GROW)
layout.Add(rb_4, flag=wx.GROW)
layout.Add(rb_5, flag=wx.GROW)

panel.SetSizer(layout)

frame.Show()
app.MainLoop()
