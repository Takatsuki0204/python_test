#! /usr/bin/python
# encoding: utf-8

import wx


def state_change_1(event):
    if checkbox_1.IsChecked():
        frame.SetStatusText("StateChange! checkbox_1")
    else:
        frame.SetStatusText("False")


def state_change_2(event):
    if checkbox_2.IsChecked():
        frame.SetStatusText("StateChange! checkbox_2")
    else:
        frame.SetStatusText("False")


def state_change(event):
    if event.GetId() == 4444:
        frame.SetStatusText("StateChange! checkbox_4")
    elif event.GetId() == 5555:
        frame.SetStatusText("StateChange! checkbox_5")

app = wx.App()
frame = wx.Frame(None, wx.ID_ANY, u"テストフレーム", size=(300, 200))
frame.CreateStatusBar()

panel = wx.Panel(frame, wx.ID_ANY)
panel.SetBackgroundColour("#AFAFAF")

checkbox_1 = wx.CheckBox(panel, wx.ID_ANY, u"チェックボックス1")
checkbox_2 = wx.CheckBox(panel, wx.ID_ANY, u"チェックボックス2")
checkbox_3 = wx.CheckBox(panel, wx.ID_ANY, u"チェックボックス3")
checkbox_4 = wx.CheckBox(panel, 4444, u"チェックボックス4")
checkbox_5 = wx.CheckBox(panel, 5555, u"チェックボックス5")

checkbox_3.SetLabel("CheckBox3")

# checkbox_3.Enable()
checkbox_3.Disable()

checkbox_2.SetToolTipString(u"チェックしてください。")

checkbox_1.Bind(wx.EVT_CHECKBOX, state_change_1)
checkbox_2.Bind(wx.EVT_CHECKBOX, state_change_2)
frame.Bind(wx.EVT_CHECKBOX, state_change, checkbox_4)
frame.Bind(wx.EVT_CHECKBOX, state_change, checkbox_5)

layout = wx.BoxSizer(wx.VERTICAL)
layout.Add(checkbox_1, flag=wx.GROW)
layout.Add(checkbox_2, flag=wx.GROW)
layout.Add(checkbox_3, flag=wx.GROW)
layout.Add(checkbox_4, flag=wx.GROW)
layout.Add(checkbox_5, flag=wx.GROW)


panel.SetSizer(layout)

frame.Show()
app.MainLoop()
