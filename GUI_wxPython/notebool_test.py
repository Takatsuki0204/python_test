#! /usr/bin/python
# encoding: utf-8

import wx

app = wx.App()
frame = wx.Frame(None, wx.ID_ANY, u"テストフレーム", size=(300, 150))

notebook = wx.Notebook(frame, wx.ID_ANY)    # フレームに対してノートブックを初期化
# notebook = wx.Notebook(frame, wx.ID_ANY, style=wx.NB_RIGHT)   # タブの位置
# notebook = wx.Notebook(frame, wx.ID_ANY, style=wx.NB_LEFT)
# notebook = wx.Notebook(frame, wx.ID_ANY, style=wx.NB_BOTTOM)

panel_1 = wx.Panel(notebook, wx.ID_ANY)  # ノートブックにパネルを初期化
panel_2 = wx.Panel(notebook, wx.ID_ANY)
panel_3 = wx.Panel(notebook, wx.ID_ANY)

panel_1.SetBackgroundColour("#FF0000")
panel_2.SetBackgroundColour("#00FF00")
panel_3.SetBackgroundColour("#0000FF")

notebook.InsertPage(0, panel_1, u"タブ1")  # ノーロブックに追加(タブの作成)
notebook.InsertPage(1, panel_2, u"タブ2")
notebook.InsertPage(2, panel_3, u"タブ3")

image_list = wx.ImageList(16, 16)   # ImageList初期化
icon = wx.Icon("RoBoHoN.ico", wx.BITMAP_TYPE_ICO)   # Icon初期化
image_list.AddIcon(icon)    # ImageListセット
notebook.AssignImageList(image_list)    # notebookにセット

notebook.SetPageImage(0, 0)  # アイコン適用(引数はタブインデックスとImageList内のインデックス)
notebook.SetPageImage(2, 0)

frame.Show()
app.MainLoop()
