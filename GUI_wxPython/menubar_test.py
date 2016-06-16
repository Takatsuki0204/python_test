#! /usr/bin/python
# encoding: utf-8

import wx

def selectMenu(event):
    frame.SetStatusText("MenuSelected! " + str(event.GetId()))

app = wx.App()
frame = wx.Frame(None, wx.ID_ANY, u"テストフレーム", size=(300, 200))
frame.CreateStatusBar()

panel = wx.Panel(frame, wx.ID_ANY)
panel.SetBackgroundColour("#AFAFAF")

menu_file = wx.Menu()
menu_file.Append(1, u"保存")
menu_file.Append(2, u"終了")

menu_file_do = wx.Menu()
menu_file_do.Append(8, u"undo")
menu_file_do.Append(9, u"redo")
menu_file.AppendSubMenu(menu_file_do, u"操作")

menu_edit = wx.Menu()
menu_edit.Append(3, u"コピー")
menu_edit.Append(4, u"貼付け")
menu_edit.AppendSeparator()  # セパレータ
check_item = menu_edit.AppendCheckItem(5, u"チェック")  # チェックボックス
check_item.Check(True)
menu_edit.AppendSeparator()  # セパレータ
menu_edit.AppendRadioItem(6, u"ラジオ1")   # ラジオボタン
menu_edit.AppendRadioItem(7, u"ラジオ2")

menu_bar = wx.MenuBar()
menu_bar.Append(menu_file, u"ファイル")
menu_bar.Append(menu_edit, u"編集")

frame.Bind(wx.EVT_MENU, selectMenu)

frame.SetMenuBar(menu_bar)

frame.Show()
app.MainLoop()
