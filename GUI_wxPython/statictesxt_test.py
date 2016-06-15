#! /usr/bin/python
# encoding: utf-8

import wx

app = wx.App()
frame = wx.Frame(None, wx.ID_ANY, u"テストフレーム", size=(300, 200))

panel = wx.Panel(frame, wx.ID_ANY)
panel.SetBackgroundColour("#AFAFAF")

# パネルへStaticText(VBでいうラベル)の追加
text_1 = wx.StaticText(panel, wx.ID_ANY, u"テキスト1")
text_2 = wx.StaticText(panel, wx.ID_ANY, u"テキスト2")
text_3 = wx.StaticText(panel, wx.ID_ANY, u"テキスト3")
text_4 = wx.StaticText(panel, wx.ID_ANY, u"テキスト4")
text_5 = wx.StaticText(panel, wx.ID_ANY, u"テキスト5")

text_3.SetLabel("Text3")    # ラベル変更

font = wx.Font(20, wx.FONTFAMILY_DEFAULT,
               wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)   # フォントサイズ変更
text_3.SetFont(font)

text_3.SetForegroundColour("#FF0000")   # フォントカラー変更
text_3.SetBackgroundColour("#00FF00")   # フォント背景カラー変更

text_3.SetToolTipString(u"ラベルです。")    # ツールチップ設定

text_4.Disable()    # 無効化
# text_3.Enable()     # 有効化
# text_3.Hide()     # 非表示
# text_3.Show()     # 表示

layout = wx.BoxSizer(wx.VERTICAL)
layout.Add(text_1)
layout.Add(text_2)
layout.Add(text_3)
layout.Add(text_4)
layout.Add(text_5)

panel.SetSizer(layout)

frame.Show()
app.MainLoop()
