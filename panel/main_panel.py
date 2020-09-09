#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: TT
@files: main_panel.py
@time: 2020/9/1 15:41
@file_desc: 
"""
import wx
from panel import utility_zone_panel, display_zone_panel


class ScreenShotMainPanel(wx.Panel):

    def __init__(self, *args, **kwargs):
        super(ScreenShotMainPanel, self).__init__(*args, **kwargs)
        self.add_tool_widget()

    def add_tool_widget(self):
        utility_zone = utility_zone_panel.UtilityPanel(self)
        display_zone = display_zone_panel.DisplayPanel(self)

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(utility_zone, 0, wx.ALL, 5)
        main_sizer.Add(display_zone, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(main_sizer)



