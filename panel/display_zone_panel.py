#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: TT
@file: display_zone_panel.py
@time: 2020/9/3 11:54
@file_desc: 
"""
import wx


class DisplayPanel(wx.Panel):

    def __init__(self, *args, **kwargs):
        super(DisplayPanel, self).__init__(*args, **kwargs)
        self.add_display_panel()

    def add_display_panel(self):
        screen_shot_bitmap = wx.Bitmap(600, 400, 100)

        screen_shot_zone = wx.StaticBitmap(self, wx.ID_ANY,
                                           screen_shot_bitmap,
                                           size=(1024, 768),
                                           style=wx.BORDER_DEFAULT)
        # 设置截屏显示区域的背景色为 灰色
        screen_shot_zone.SetBackgroundColour(wx.Colour(192, 192, 192))

        display_sizer = wx.BoxSizer(wx.VERTICAL)
        display_sizer.SetMinSize(800, 600)
        display_sizer.Add(screen_shot_zone, 0, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(display_sizer)

