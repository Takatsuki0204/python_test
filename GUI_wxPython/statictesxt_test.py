#! /usr/bin/python
# encoding: utf-8

import wx

app = wx.App()
frame = wx.Frame(None, wx.ID_ANY, u"テストフレーム", size=(300, 200))

panel = wx.Panel(frame, wx.ID_ANY)
panel.SetBackgroundColour("#AFAFAF")

# パネルへStaticText(VBでいうラベル)の追加
text_1 = wx.StaticText(panel, wx.ID_ANY, u"テキスト1")
t = wx.StaticText(panel, wx.ID_ANY, "")  # 1行開ける場合の小技
text_2 = wx.StaticText(panel, wx.ID_ANY, u"テキスト2")
text_3 = wx.StaticText(panel, wx.ID_ANY, u"テキスト3", style=wx.TE_LEFT)
text_4 = wx.StaticText(panel, wx.ID_ANY, u"テキスト4", style=wx.TE_CENTER)
text_5 = wx.StaticText(panel, wx.ID_ANY, u"テキスト5", style=wx.TE_RIGHT)

text_3.SetLabel("Text3")    # ラベル変更

font = wx.Font(20, wx.FONTFAMILY_DEFAULT,
               wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)   # フォントサイズ変更
text_3.SetFont(font)

text_3.SetForegroundColour("#FF0000")   # フォントカラー変更
text_3.SetBackgroundColour("#00FF00")   # フォント背景カラー変更

text_3.SetToolTipString(u"ラベルです。")    # ツールチップ設定

text_2.Disable()    # 無効化
# text_3.Enable()     # 有効化
# text_3.Hide()     # 非表示
# text_3.Show()     # 表示

layout = wx.BoxSizer(wx.VERTICAL)
layout.Add(text_1, flag=wx.GROW)
layout.Add(t, flag=wx.GROW)
layout.Add(text_2, flag=wx.GROW)
layout.Add(text_3, flag=wx.GROW)
layout.Add(text_4, flag=wx.GROW)
layout.Add(text_5, flag=wx.GROW)

panel.SetSizer(layout)

frame.Show()
app.MainLoop()
