#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: TT
@files: text_panel.py
@time: 2020/9/1 13:43
@file_desc: 
"""
import wx


class TextCopyPastePanel(wx.Panel):
    
    def __init__(self, *args, **kwargs):
        super(TextCopyPastePanel, self).__init__(*args, **kwargs)
        self.left = self.left_text()
        self.right = self.right_text()
        self.add_tool_zone()

    def add_tool_zone(self):
        left_txt = self.left
        right_txt = self.right
        btn_copy = self.btn_copy()
        btn_paste = self.btn_paste()

        sizer = wx.BoxSizer(wx.HORIZONTAL)

        items = (left_txt, right_txt, btn_copy, btn_paste,)

        sizer.AddMany(items)
        self.SetSizer(sizer)

        self.Bind(wx.EVT_BUTTON, self.evt_on_copy, btn_copy)
        self.Bind(wx.EVT_BUTTON, self.evt_on_paste, btn_paste)

    def left_text(self):
        left_txt = """
        这个文本区域存放的是需要被复制的文本内容，
        点击复制按钮即可复制该区域的文本内容
                    """
        left = wx.TextCtrl(self, wx.ID_ANY, value=left_txt, size=(300, 300), style=wx.TE_MULTILINE | wx.HSCROLL)
        return left

    def right_text(self):
        right_txt = """
                    该区域用于存放粘贴从剪切板复制过来的文本内容
                    """
        right = wx.TextCtrl(self, wx.ID_ANY, value=right_txt, size=(300, 300), style=wx.TE_MULTILINE | wx.HSCROLL)
        return right

    def btn_copy(self):
        btn_copy = wx.Button(self, wx.ID_ANY, label="复制文本")
        return btn_copy

    def btn_paste(self):
        btn_paste = wx.Button(self, wx.ID_ANY, label="粘贴文本")
        return btn_paste

    def evt_on_copy(self, event):
        print("开始复制文本内容")
        data = wx.TextDataObject()
        data.SetText(self.left.GetValue())
        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(data)
            wx.TheClipboard.Close()
            print("已成功复制到文本内容")
        else:
            wx.MessageBox("Unable to open clipboard", "Error")

    def evt_on_paste(self, event):
        print("粘贴复制的文本内容")
        success = False
        data = wx.TextDataObject()
        if wx.TheClipboard.Open():
            success = wx.TheClipboard.GetData(data)
            wx.TheClipboard.Close()

        if success:
            self.right.SetValue(data.GetText())
            print("成功粘贴文本内容")
        else:
            wx.MessageBox("There is no data in clipboard in the required format", "Error")
