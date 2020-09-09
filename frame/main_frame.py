#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: TT
@files: main_frame.py
@time: 2020/9/1 13:59
@file_desc: 
"""
from panel import main_panel
import wx


class ScreenShotFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(ScreenShotFrame, self).__init__(*args, **kwargs)
        self.add_tool_panel()

    def add_tool_panel(self):
        main_panel.ScreenShotMainPanel(self)


