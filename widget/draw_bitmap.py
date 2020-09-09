#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: TT
@file: draw_bitmap.py
@time: 2020/9/3 14:13
@file_desc: 
"""
import wx
import random
import os

random.seed()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGE_DIR = os.path.join(BASE_DIR, "static/images").replace("\\", "/")


class DrawBitmap(wx.Window):

    def __init__(self, parent, image):
        super(DrawBitmap, self).__init__(parent)
        self.photo = image.ConvertToBitmap()
        self.position = [(10, 10)]
        # for x in range(50):
        #     x = random.randint(0, 1000)
        #     y = random.randint(0, 1000)
        #     self.position.append((x, y))
        self.Bind(wx.EVT_PAINT, self.on_paint)

    def on_paint(self, event):
        dc = wx.PaintDC(self)
        # dc = wx.ScreenDC()
        brush = wx.Brush("gray")
        dc.SetBackground(brush)

        dc.Clear()
        for x, y in self.position:
            dc.DrawBitmap(self.photo, x, y, True)


class DrawBitMapFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title="Draw Bitmap", size=(640, 480))
        image_name = os.path.join(IMAGE_DIR, "newton.jpg").replace("\\", "/")
        img = wx.Image(image_name, wx.BITMAP_TYPE_ANY)
        win = DrawBitmap(self, img)
        # self.Iconize(True)


if __name__ == "__main__":
    app = wx.App()
    frm = DrawBitMapFrame()
    frm.Show()
    app.MainLoop()

