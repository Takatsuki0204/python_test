#! /usr/bin/python
# encoding: utf-8

import wx

app = wx.App()
frame = wx.Frame(None, wx.ID_ANY, u"テストフレーム", size=(300, 200))

panel = wx.Panel(frame, wx.ID_ANY)
panel.SetBackgroundColour("#AFAFAF")

t_button_1 = wx.ToggleButton(panel, wx.ID_ANY, u"トグルボタン1")
t_button_2 = wx.ToggleButton(panel, wx.ID_ANY, u"トグルボタン2", size=(150, 50))
t_button_3 = wx.ToggleButton(panel, wx.ID_ANY, u"トグルボタン3")

t_button_2.SetLabel("ToggleButton2")

font = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
t_button_2.SetFont(font)

# t_button_2.Enable()
# t_button_2.Disable()

layout = wx.BoxSizer(wx.VERTICAL)
layout.Add(t_button_1, flag=wx.GROW)
layout.Add(t_button_2)
layout.Add(t_button_3, flag=wx.GROW)

panel.SetSizer(layout)

frame.Show()
app.MainLoop()