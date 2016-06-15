#! /usr/bin/python
# encoding: utf-8

import wx

# フレームを継承したトップレベルウィンドウクラス


class CalcFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, u"電卓", size=(300, 200))

        # ステータスバーの初期化
        self.CreateStatusBar()
        self.SetStatusText("calculator_test")
        self.GetStatusBar().SetBackgroundColour(None)

        # メニューバーの初期化
        self.SetMenuBar(CalcMenu())

        # 本体部分の構築
        root_panel = wx.Panel(self, wx.ID_ANY)

        text_panel = CommandButtonPanel(root_panel)
        cmdbutton_panel = CommandButtonPanel(root_panel)
        calcbutton_panel = CalcButtonPanel(root_panel)

        root_layout = wx.BoxSizer(wx.VERTICAL)
        root_layout.Add(text_panel, 0, wx.GROW | wx.ALL, border=10)
        root_layout.Add(cmdbutton_panel, 0, wx.GROW |
                        wx.LEFT | wx.RIGHT, border=20)
        root_layout.Add(calcbutton_panel, 0, wx.GROW | wx.ALL, border=10)
        root_panel.SetSizer(root_layout)
        root_layout.Fit(root_panel)

# CalcFrameにセットするメニューバークラス


class CalcMenu(wx.MenuBar):

    def __init__(self):
        wx.MenuBar.__init__(self)

        menu_file = wx.Menu()
        menu_file.Append(wx.ID_ANY, u"保存")
        menu_file.Append(wx.ID_ANY, u"終了")
        menu_edit = wx.Menu()
        menu_edit.Append(wx.ID_ANY, u"コピー")
        menu_edit.Append(wx.ID_ANY, u"ペースト")

        self.Append(menu_file, u"ファイル")
        self.Append(menu_edit, u"編集")

# 画面上部に表示されるテキスト部分


class TextPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, wx.ID_ANY)

        calc_text = wx.TextCtrl(self, wx.ID_NAY, style=wx.TE_RIGHT)
        layout = wx.BoxSizer(wx, HORIZONTAL)
        layout.Add(calc_text, 1)
        self.SetSizer(layout)

# 画面中部に表示されるボタン部分
