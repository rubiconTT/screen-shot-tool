#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: TT
@file: drag.py
@time: 2020/9/2 14:01
@file_desc: 
"""
import wx


class DragController(wx.Control):
    def __init__(self, parent, source, size=wx.Size(25, 25)):
        wx.Control.__init__(self, parent, wx.ID_ANY, size=size, style=wx.SIMPLE_BORDER)
        self.source = source
        self.SetMinSize(size)
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Bind(wx.EVT_LEFT_DOWN, self.on_left_down)

    def on_paint(self, event):
        dc = wx.BufferedPaintDC(self)
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        width, height = dc.GetSize()
        y = height/2
        dc.SetPen(wx.Pen("dark blue", 2))
        dc.DrawLine(width/8, y, width-width/8, y)
        dc.DrawLine(width-width/8, y, width/2, height/2)
        dc.DrawLine(width-width/8, y, width/2, 3*height/4)

    def on_left_down(self, event):
        text = self.source.GetValue()
        data = wx.TextDataObject(text)
        drop_source = wx.DropSource(self)
        drop_source.SetData(data)
        result = drop_source.DoDragDrop(wx.Drag_AllowMove)
        if result == wx.DragMove:
            self.source.SetValue("")


class WidgetFrame(wx.Frame):
    def __init__(self):
        super(WidgetFrame, self).__init__(None, title="Drag Widget")

        p = wx.Panel(self)

        label1 = wx.StaticText(p, wx.ID_ANY, "put some text in this control:")
        label2 = wx.StaticText(p, wx.ID_ANY, "Then drag from the neighboring bitmap and\n"
                               "drop in an application that accepts dropped\n"
                               "text, such as MS Word.")
        text = wx.TextCtrl(p, wx.ID_ANY, "Some Text")
        drag_ctrl = DragController(p, text)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(label1, 0, wx.ALL, 5)
        hrow = wx.BoxSizer(wx.HORIZONTAL)
        hrow.Add(text, 1, wx.RIGHT, 5)
        hrow.Add(drag_ctrl, 0)
        sizer.Add(hrow, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(label2, 0, wx.ALL, 5)
        p.SetSizer(sizer)
        sizer.Fit(self)


if __name__ == "__main__":
    app = wx.App()
    frm = WidgetFrame()
    frm.Show()
    app.MainLoop()

