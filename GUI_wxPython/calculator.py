#! /usr/bin/python
# encoding: utf-8

import wx

# フレームを継承したトップレベルウィンドウクラス
class CalcFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, u"電卓", size=(300, 280))

        # ステータスバーの初期化
        self.CreateStatusBar()
        self.SetStatusText("calculator_test")
        self.GetStatusBar().SetBackgroundColour(None)

        # メニューバーの初期化
        self.SetMenuBar(CalcMenu())

        # 本体部分の構築
        root_panel = wx.Panel(self, wx.ID_ANY)

        text_panel = TextPanel(root_panel)
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
        menu_file.Append(1, u"保存")
        menu_file.Append(2, u"終了")
        menu_edit = wx.Menu()
        menu_edit.Append(3, u"コピー")
        menu_edit.Append(4, u"ペースト")

        self.Append(menu_file, u"ファイル")
        self.Append(menu_edit, u"編集")

        self.Bind(wx.EVT_MENU, self.selectMenu)
    
    def selectMenu(self, event):
        if event.GetId() == 2:
            exit()

# 画面上部に表示されるテキスト部分
class TextPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, wx.ID_ANY)

        calc_text = wx.TextCtrl(self, wx.ID_ANY, style=wx.TE_RIGHT)
        layout = wx.BoxSizer(wx.HORIZONTAL)
        layout.Add(calc_text, 1)
        self.SetSizer(layout)

# 画面中部に表示されるボタン部分
class CommandButtonPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, wx.ID_ANY)

        button_ce = wx.Button(self, 11, "CE")
        button_c = wx.Button(self, 22, "C")
        layout = wx.BoxSizer(wx.HORIZONTAL)
        layout.Add(button_ce, flag=wx.GROW)
        layout.Add(button_c, flag=wx.GROW)
        self.SetSizer(layout)

# 画面下部に表示されるボタン部分
class CalcButtonPanel(wx.Panel):

    def __init__(self, parent):
        count = 1
        wx.Panel.__init__(self, parent, wx.ID_ANY)
        
        button_collection = ("7", "8", "9", "/",
                             "4", "5", "6", "*",
                             "1", "2", "3", "-",
                             "0", ".", "=", "+")

        layout = wx.GridSizer(4, 4, 3, 3)

        for i in button_collection:
            layout.Add(wx.Button(self, count, i,
                                 size=(30, 25)), 1, wx.GROW)
            count += 1
        
        self.SetSizer(layout)

# カスタムフレームを初期化してアプリケーションを開始
if __name__ == "__main__":

    app = wx.App()
    frame = CalcFrame()
    frame.Show()
    app.MainLoop()
