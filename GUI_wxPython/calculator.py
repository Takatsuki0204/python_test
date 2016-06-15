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
        root_layout.Add(cmdbutton_panel, 0, wx.GROW | wx.LEFT | wx.RIGHT, border=20)
        root_layout.Add(calcbutton_panel, 0, wx.GROW | wx.ALL, border=10)
        root_panel.SetSizer(root_layout)
        root_layout.Fit(root_panel)

# CalcFrameにセットするメニューバークラス