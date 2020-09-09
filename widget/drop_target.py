#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: TT
@file: drop_target.py
@time: 2020/9/2 14:26
@file_desc: 
"""
import wx


class CustomDropTarget(wx.DropTarget):

    def __init__(self, data):

        self.data_object = wx.CustomDataObject(format("CustomDataObj"))
        self.data_object.SetData(data)
        super(CustomDropTarget, self).__init__(self.data_object)

    def OnData(self, x, y, defResult):
        self.GetData()
        actual_data = self.data_object.GetData()
        return defResult


class CustomDocFileDropTarget(wx.FileDropTarget):

    def __init__(self, window):
        super(CustomDocFileDropTarget, self).__init__()
        self.window = window

    def OnDropFiles(self, x, y, filenames):
        self.window.AppendText("\n%d file(s) dropped at (%d,%d):\n" % (len(filenames), x, y))
        for file_name in filenames:
            self.window.AppendText("\t%s\n" % file_name)
        return True


class CustomImageFileDropTarget(wx.FileDropTarget):

    def __init__(self, window):
        super(CustomImageFileDropTarget, self).__init__()
        self.window = window

    def OnEnter(self, x, y, defResult):
        print("拖放文件正在进入,首先执行OnEnter方法,def result:", defResult)
        return defResult

    def OnDragOver(self, x, y, defResult):
        print("拖放的文件正在窗口上方悬停,其次执行OnDragOver方法,def result:", defResult)
        return defResult

    def OnDropFiles(self, x, y, filenames):
        print("文件已经被放置在窗口当中,再次执行OnDropFiles方法.....")
        for file_name in filenames:
            bitmap = wx.Bitmap(file_name, wx.BITMAP_TYPE_ANY)
            self.window.SetBitmap(bitmap)
        return True

    def OnLeave(self):
        print("文件已经拖放到位，正在离开,最后执行OnLeave方法")


class DropTargetFrame(wx.Frame):

    def __init__(self):
        super(DropTargetFrame, self).__init__(parent=None, title="File Drop Target", size=wx.Size(500, 300))
        p = wx.Panel(self)

        label = wx.StaticText(p, wx.ID_ANY, "Drop some files here:")
        text = wx.TextCtrl(p, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.HSCROLL)
        bitmap = wx.StaticBitmap(p, wx.ID_ANY, wx.Bitmap())

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(label, 0, wx.ALL, 5)
        sizer.Add(text, 1, wx.EXPAND | wx.ALL, 5)
        sizer.Add(bitmap, 2, wx.EXPAND | wx.ALL, 5)

        p.SetSizer(sizer)

        dt = CustomDocFileDropTarget(text)
        text.SetDropTarget(dt)
        dt2 = CustomImageFileDropTarget(bitmap)
        bitmap.SetDropTarget(dt2)


if __name__ == "__main__":
    app = wx.App()
    frm = DropTargetFrame()
    frm.Show()
    app.MainLoop()





