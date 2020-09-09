#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: TT
@files: screenshot.py
@time: 2020/9/1 13:37
@file_desc: 
"""
from frame import main_frame
import wx
app = wx.App()
frm = main_frame.ScreenShotFrame(None, title="Screen Shot Tool", size=(800, 600))
frm.Show()
app.MainLoop()
