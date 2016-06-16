#! /usr/bin/python
# encoding: utf-8

import wx

app = wx.App()
frame = wx.Frame(None, wx.ID_ANY, u"テストフレーム", size=(300, 400))
frame.CreateStatusBar()

panel = wx.Panel(frame, wx.ID_ANY)
panel.SetBackgroundColour("#AFAFAF")

text_1 = wx.TextCtrl(panel, wx.ID_ANY)
text_2 = wx.TextCtrl(panel, wx.ID_ANY, u"左寄せ", style=wx.TE_LEFT)
text_3 = wx.TextCtrl(panel, wx.ID_ANY, u"中央寄せ", style=wx.TE_CENTER)
text_4 = wx.TextCtrl(panel, wx.ID_ANY, u"右寄せ",
                     style=wx.TE_RIGHT | wx.TE_MULTILINE)   # 複数行入力可能にできる
text_5 = wx.TextCtrl(panel, wx.ID_ANY, u"テキスト1")
text_6 = wx.TextCtrl(panel, wx.ID_ANY, u"テキスト2")
text_7 = wx.TextCtrl(panel, wx.ID_ANY, u"テキスト3")
text_8 = wx.TextCtrl(panel, wx.ID_ANY, u"テキスト4")
text_9 = wx.TextCtrl(panel, wx.ID_ANY, u"テキスト5")
text_10 = wx.TextCtrl(panel, wx.ID_ANY, u"テキスト6")

text_1.SetMaxLength(10) # 最大文字数の設定
# SetValueで超過して入力可能

# print text_10.GetValue()
# print text_9.GetStringSelection()
# print text_8.GetRange(2, 5)

font = wx.Font(20, wx.FONTFAMILY_DEFAULT,
               wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
text_4.SetFont(font)
text_4.SetForegroundColour("#FF0000")   # 文字色変更
text_4.SetBackgroundColour("#00FF00")   # 背景色変更

# text_3.Enable()    # 有効
text_3.Disable()    # 無効

text_5.SetValue("text1")    # 上書き
text_6.WriteText("text2")   # 前に追加
text_7.AppendText("text3")  # 後ろに追加
text_8.Clear()  # 文字列削除
text_9.Remove(2, 3)  # 指定文字数削除
text_10.Replace(2, 3, u"す")  # 置き換え

layout = wx.BoxSizer(wx.VERTICAL)
layout.Add(text_1, flag=wx.GROW)
layout.Add(text_2, flag=wx.GROW)
layout.Add(text_3, flag=wx.GROW)
layout.Add(text_4, flag=wx.GROW)
layout.Add(text_5, flag=wx.GROW)
layout.Add(text_6, flag=wx.GROW)
layout.Add(text_7, flag=wx.GROW)
layout.Add(text_8, flag=wx.GROW)
layout.Add(text_9, flag=wx.GROW)
layout.Add(text_10, flag=wx.GROW)

panel.SetSizer(layout)

frame.Show()
app.MainLoop()
