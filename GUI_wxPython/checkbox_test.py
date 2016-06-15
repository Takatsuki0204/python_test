#! /usr/bin/python
# encoding: utf-8

import wx

def state_change_1(event):
    frame.SetStatusText("StateChange! checkbox_1")

def state_change_2(event):
    frame.SetStatusText("StateChange! checkbox_2")

app = wx.App()
frame = wx.Frame(None, wx.ID_ANY, u"テストフレーム", size=(300, 200))
frame.SetStatusBar()

panel = wx.Panel(frame, wx.ID_ANY)
panel.SetBackgroundColour("#AFAFAF")

checkbox_1 = wx.CheckBox(panel, wx.ID_ANY, u"チェックボックス1")
checkbox_2 = wx.CheckBox(panel, wx.ID_ANY, u"チェックボックス2")
checkbox_3 = wx.CheckBox(panel, wx.ID_ANY, u"チェックボックス3")
checkbox_4 = wx.CheckBox(panel, wx.ID_ANY, u"チェックボックス4")
checkbox_5 = wx.CheckBox(panel, wx.ID_ANY, u"チェックボックス5")

checkbox_3.SetLabel("CheckBox3")

# checkbox_3.Enable()
checkbox_3.Disable()

checkbox_2.SetToolTipString(u"チェックしてください。")

layout = wx.BoxSizer(wx.VERTICAL)
layout.Add(checkbox_1, flag=wx.GROW)
layout.Add(checkbox_2, flag=wx.GROW)
layout.Add(checkbox_3, flag=wx.GROW)
layout.Add(checkbox_4, flag=wx.GROW)
layout.Add(checkbox_5, flag=wx.GROW)


panel.SetSizer(layout)

frame.Show()
app.MainLoop()