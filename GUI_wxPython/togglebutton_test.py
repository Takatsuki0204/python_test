#! /usr/bin/python
# encoding: utf-8

import wx

def click_togglebutton_1(event):
    frame.SetStatusText("Click! Toggle1")

def click_toggle(event):
    if event.GetId() == 333:
        frame.SetStatusText("Click! Toggle3")
    elif event.GetId() == 444:
        frame.SetStatusText("Click! Toggle4")

app = wx.App()
frame = wx.Frame(None, wx.ID_ANY, u"テストフレーム", size=(300, 200))
frame.CreateStatusBar()

panel = wx.Panel(frame, wx.ID_ANY)
panel.SetBackgroundColour("#AFAFAF")

t_button_1 = wx.ToggleButton(panel, wx.ID_ANY, u"トグルボタン1")
t_button_2 = wx.ToggleButton(panel, wx.ID_ANY, u"トグルボタン2", size=(150, 50))
t_button_3 = wx.ToggleButton(panel, 333, u"トグルボタン3")
t_button_4 = wx.ToggleButton(panel, 444, u"トグルボタン4")

t_button_2.SetLabel("ToggleButton2")

font = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
t_button_2.SetFont(font)

# t_button_2.Enable()
# t_button_2.Disable()
# t_button_2.Hide()
# t_button_2.Show()

t_button_1.SetToolTipString(u"選択してください。")

t_button_1.Bind(wx.EVT_TOGGLEBUTTON, click_togglebutton_1)
frame.Bind(wx.EVT_TOGGLEBUTTON, click_toggle, t_button_3)
frame.Bind(wx.EVT_TOGGLEBUTTON, click_toggle, t_button_4)

t_button_2.SetValue(True)
print t_button_1.GetValue()

layout = wx.BoxSizer(wx.VERTICAL)
layout.Add(t_button_1, flag=wx.GROW)
layout.Add(t_button_2)
layout.Add(t_button_3, flag=wx.GROW)
layout.Add(t_button_4, flag=wx.GROW)

panel.SetSizer(layout)

frame.Show()
app.MainLoop()