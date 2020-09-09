#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: TT
@files: bitmap_panel.py
@time: 2020/9/1 15:44
@file_desc: 
"""
import wx
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGE_DIR = os.path.join(BASE_DIR, "static/images").replace("\\", "/")


class BitmapCopyPastePanel(wx.Panel):

    def __init__(self, *args, **kwargs):
        super(BitmapCopyPastePanel, self).__init__(*args, **kwargs)
        self.left = self.left_bitmap()
        self.right = self.right_bitmap()
        self.add_tool_zone()

    def add_tool_zone(self):
        left_bm = self.left
        right_bm = self.right
        btn_copy = self.btn_copy()
        btn_paste = self.btn_paste()

        sizer = wx.BoxSizer(wx.HORIZONTAL)

        items = (left_bm, right_bm, btn_copy, btn_paste,)

        sizer.AddMany(items)
        self.SetSizer(sizer)

        self.Bind(wx.EVT_BUTTON, self.evt_on_copy, btn_copy)
        self.Bind(wx.EVT_BUTTON, self.evt_on_paste, btn_paste)

    def left_bitmap(self):

        image_name = os.path.join(IMAGE_DIR, "Aoo20.ico").replace("\\", "/")
        print("image name:", image_name)
        left_img = wx.Image(image_name, wx.BITMAP_TYPE_ANY)
        left_bitmap = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(left_img))

        return left_bitmap

    def right_bitmap(self):
        image_name = os.path.join(IMAGE_DIR, "Aoo5.ico").replace("\\", "/")
        right_bitmap = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(image_name, wx.BITMAP_TYPE_ANY))
        return right_bitmap

    def btn_copy(self):
        btn_copy = wx.Button(self, wx.ID_ANY, label="复制位图")
        return btn_copy

    def btn_paste(self):
        btn_paste = wx.Button(self, wx.ID_ANY, label="粘贴位图")
        return btn_paste

    def evt_on_copy(self, event):
        print("开始复制位图")

        data = wx.BitmapDataObject()
        data.SetBitmap(self.left.GetBitmap())
        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(data)
            wx.TheClipboard.Close()
            print("已成功复制到位图")
        else:
            wx.MessageBox("Unable to open clipboard", "Error")

    def evt_on_paste(self, event):
        print("粘贴复制的位图")
        success = False
        data = wx.BitmapDataObject()
        if wx.TheClipboard.Open():
            success = wx.TheClipboard.GetData(data)
            wx.TheClipboard.Close()

        if success:
            self.right.SetBitmap(data.GetBitmap())
            print("成功粘贴位图内容")
        else:
            wx.MessageBox("There is no data in clipboard in the required format", "Error")
