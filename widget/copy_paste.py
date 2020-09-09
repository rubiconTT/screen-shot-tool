#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: TT
@file: copy_paste.py
@time: 2020/9/3 11:32
@file_desc: 
"""
import wx
from panel import text_panel
from panel import bitmap_panel


class CopyAndPaste(wx.Panel):

    def __init__(self, *args, **kwargs):
        super(CopyAndPaste, self).__init__(*args, **kwargs)
        self.add_utility_zone()

    def add_utility_zone(self):

        txt_panel = text_panel.TextCopyPastePanel(self)
        bit_panel = bitmap_panel.BitmapCopyPastePanel(self)
        items = (txt_panel, bit_panel,)

        main_panel_sizer = wx.BoxSizer(wx.VERTICAL)
        main_panel_sizer.AddMany(items)

        self.SetSizer(main_panel_sizer)


if __name__ == "__main__":
    app = wx.App()
    frm = wx.Frame(None, title="Text & Bitmap Copy and Paste", size=wx.Size(800, 600))
    panel = CopyAndPaste(frm)

    frm.Show()
    app.MainLoop()
