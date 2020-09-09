#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: TT
@file: screen_handle_frame.py
@time: 2020/9/4 13:56
@file_desc: 
"""
import wx
import ctypes


class GrabFrame(wx.Frame):

    def __init__(self, main_frame):
        wx.Frame.__init__(self,
                          main_frame,
                          wx.NewId(),
                          pos=(0, 0),
                          size=wx.Size(1920, 1080),
                          style=wx.NO_BORDER | wx.STAY_ON_TOP)

        # 矩形截图的起止点
        self.firstPoint = wx.Point(0, 0)
        self.lastPoint = wx.Point(0, 0)
        # 记录是否按下鼠标左键
        self.started = False
        # 当前frame的父frame
        self.frame = main_frame
        # 当前windows窗口中的全屏位图
        self.frame.fullBmp = GrabFrame.full_screen_bitmap()

        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)

        self.bind_event()

    def bind_event(self):
        # 绘图事件 默认Frame创建完成之后就会执行
        self.Bind(wx.EVT_PAINT, self.on_paint)
        # 鼠标按放与拖动事件
        self.Bind(wx.EVT_LEFT_DOWN, self.on_mouse_left_down)
        self.Bind(wx.EVT_LEFT_UP, self.on_mouse_left_up)
        self.Bind(wx.EVT_MOTION, self.on_mouse_move)
        # 鼠标右键与ESC键 取消截屏事件
        self.Bind(wx.EVT_RIGHT_DOWN, self.on_mouse_right_down)
        self.Bind(wx.EVT_KEY_DOWN, self.evt_key_esc_down)

    def on_paint(self, evt):
        dc = wx.GCDC(wx.BufferedPaintDC(self))
        self.paint_update(dc)

    def paint_update(self, dc):
        rect = self.GetClientRect()
        print("client rect:", rect)
        color = wx.Colour(0, 0, 0, 120)

        # 设置绘制截图区域时矩形的点
        min_x, min_y = min(self.firstPoint.x, self.lastPoint.x), min(self.firstPoint.y, self.lastPoint.y)
        max_x, max_y = max(self.firstPoint.x, self.lastPoint.x), max(self.firstPoint.y, self.lastPoint.y)
        
        max_point = wx.Point(max_x, max_y)
        min_point = wx.Point(min_x, min_y)
        
        self.paint_screen_shot_bg(dc, rect, color, max_point, min_point)

        if self.started:
            self.paint_screen_shot_zone(dc, color, max_point, min_point)

    def paint_screen_shot_bg(self, dc, rect, color, max_point, min_point):
        max_x = max_point.x
        max_y = max_point.y
        min_x = min_point.x
        min_y = min_point.y
        # 画出整个屏幕的截图
        # full_screen_bmp = self.full_screen_bitmap()
        dc.DrawBitmap(self.frame.fullBmp, 0, 0, False)
        # 剔除截图区域后，剩余的四块阴影区域
        # 如果还没有开始使用鼠标进行拖拽，则为整个屏幕截图
        dc.SetPen(wx.Pen(color))
        dc.SetBrush(wx.Brush(color))
        dc.DrawRectangle(0, 0, max_x, min_y)
        dc.DrawRectangle(max_x, 0, rect.width - max_x, max_y)
        dc.DrawRectangle(min_x, max_y, rect.width - min_x, rect.height - max_y)
        dc.DrawRectangle(0, min_y, min_x, rect.height - min_y)
    
    def paint_screen_shot_zone(self, dc, color, max_point, min_point):
        max_x = max_point.x
        max_y = max_point.y
        min_x = min_point.x
        min_y = min_point.y
        # 画出截图区域
        dc.SetPen(wx.Pen(wx.Colour(255, 0, 0)))
        dc.SetBrush(wx.Brush(color, style=wx.TRANSPARENT))
        dc.DrawRectangle(min_x, min_y, max_x - min_x, max_y - min_y)
        # 截图区域的具体信息
        self.draw_screen_shot_zone_info(dc, max_point, min_point)

    def draw_screen_shot_zone_info(self, dc, max_point, min_point):
        max_x = max_point.x
        max_y = max_point.y
        min_x = min_point.x
        min_y = min_point.y
        # 显示截图部分的位置信息
        color = wx.Colour(0, 0, 0, 0)
        w, h = 140, 43
        # 截图区域具体的显示信息
        s = u'区域大小: (' + str(max_x - min_x) + ' * ' + str(max_y - min_y) + ')'
        s += u'\n鼠标位置: (' + str(self.lastPoint.x) + ' , ' + str(self.lastPoint.y) + ')'
        # 显示区域的矩形框
        dc.SetPen(wx.Pen(color))
        dc.SetBrush(wx.Brush(color, wx.SOLID))
        dc.DrawRectangle(min_x, (min_y - h - 5 if min_y - 5 > h else min_y + 5), w, h)
        # 文字前景色
        dc.SetTextForeground(wx.Colour(0, 255, 0))
        # 文字
        dc.DrawText(s, min_x + 5, (min_y - h - 5 if min_y - 5 > h else min_y + 5) + 5)

    def on_mouse_left_down(self, evt):
        self.started = True
        self.firstPoint = evt.GetPosition()
        self.lastPoint = evt.GetPosition()

    def on_mouse_left_up(self, evt):
        if self.started:
            self.lastPoint = evt.GetPosition()
            if (self.firstPoint.x == self.lastPoint.x) and \
                    (self.firstPoint.y == self.lastPoint.y):
                self.redraw_screen_shot()
            else:
                screen_shot_bitmap = self.get_screen_shot_bitmap()
                self.show_screen_shot(screen_shot_bitmap)

    def redraw_screen_shot(self):
        wx.MessageBox("区域设置不正确", "Error")
        self.started = False
        self.firstPoint = wx.Point(0, 0)
        self.lastPoint = wx.Point(0, 0)

    def get_screen_shot_bitmap(self):
        screen_shot_bitmap = self.frame.fullBmp.GetSubBitmap(wx.Rect(
            min(self.firstPoint.x, self.lastPoint.x),
            min(self.firstPoint.y, self.lastPoint.y),
            abs(self.firstPoint.x - self.lastPoint.x),
            abs(self.firstPoint.y - self.lastPoint.y)
        ))
        return screen_shot_bitmap

    def on_mouse_move(self, evt):
        if self.started:
            self.lastPoint = evt.GetPosition()
            self.RefreshRect(self.GetClientRect(), True)
            self.Update()

    def on_mouse_right_down(self, event):
        print("右键被按下")
        self.cancel_screen_shot()

    def evt_key_esc_down(self, event):
        print("ESC键被按下")
        key_esc = event.GetKeyCode()
        print("current key code:", key_esc)
        if key_esc == wx.WXK_ESCAPE:
            self.cancel_screen_shot()

    def show_screen_shot(self, bitmap):
        self.Destroy()
        self.frame.Iconize(False)
        self.frame.GetChildren()[0].GetChildren()[1].GetChildren()[0].SetBitmap(bitmap)

    def cancel_screen_shot(self):
        self.Destroy()
        self.frame.Iconize(False)

    @staticmethod
    def full_screen_bitmap():

        # s = wx.GetDisplaySize()
        s = wx.Size(1920, 1080)
        # ppi = wx.GetDisplayPPI()
        # print("ppi:", ppi)

        print("S:", s)
        bmp = wx.Bitmap(s.x, s.y)
        # 处理win10 DPI 对应wxpython的缩放模糊问题,通常为2， 如果设置为0，则会减小 DPI
        err_code = ctypes.windll.shcore.SetProcessDpiAwareness(2)
        print("1 err code:", err_code)
        # 打印整个屏幕内容
        dc = wx.ScreenDC()
        memory_dc = wx.MemoryDC(dc)

        memory_dc.SelectObject(bmp)
        memory_dc.Blit(0, 0, s.x, s.y, dc, 0, 0)
        memory_dc.SelectObject(wx.NullBitmap)
        print("bmp size:", bmp.GetSize())
        return bmp
