#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: TT
@file: utility_zone_panel.py
@time: 2020/9/3 11:53
@file_desc: 
"""
import wx
import os
import time
import random
from frame import screen_handle_frame

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGE_DIR = os.path.join(BASE_DIR, "static/images").replace("\\", "/")


class UtilityPanel(wx.Panel):

    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        self.bmp = None
        self.add_utility_btn()

    def add_utility_btn(self):
        btn_screen_shot = wx.Button(self, wx.ID_ANY, "截屏", size=(80, 50))
        btn_save = wx.Button(self, wx.ID_ANY, "保存", size=(80, 50))
        btn_clear = wx.Button(self, wx.ID_ANY, "清除", size=(80, 50))

        btn_screen_shot.SetBackgroundColour(wx.Colour(0, 128, 0))
        btn_save.SetBackgroundColour(wx.Colour(128, 0, 128))
        btn_clear.SetBackgroundColour(wx.Colour(128, 0, 255))

        btn_items = (btn_screen_shot, btn_save, btn_clear)

        utility_sizer = wx.BoxSizer(wx.HORIZONTAL)
        utility_sizer.AddMany(btn_items)

        self.SetSizer(utility_sizer)

        self.Bind(wx.EVT_BUTTON, self.evt_btn_screen_shot, btn_screen_shot)
        self.Bind(wx.EVT_BUTTON, self.evt_btn_save, btn_save)
        self.Bind(wx.EVT_BUTTON, self.evt_btn_clear, btn_clear)

    def evt_btn_screen_shot(self, event):
        # 首先最小化功能窗口
        main_window = self.GetTopLevelParent()
        main_window.Iconize(True)
        time.sleep(0.2)
        if main_window.IsIconized():
            # 整个屏幕加上遮罩作为截屏的初始界面显示
            handle_frame = screen_handle_frame.GrabFrame(main_window)
            handle_frame.Show()

    def evt_btn_save(self, event):
        display = self.GetParent().GetChildren()[1].GetChildren()[0]
        need_save_bitmap = display.GetBitmap()
        self.save_screen_shot_bmp(need_save_bitmap)

    def evt_btn_clear(self, event):
        """
        清空截屏显示界面
        :param event:
        :type event:
        :return:
        :rtype:
        """
        display = self.GetParent().GetChildren()[1].GetChildren()[0]
        display.SetBitmap(wx.Bitmap())

    def save_screen_shot_bmp(self, need_save_bitmap):
        if not (need_save_bitmap is None) and need_save_bitmap != 0 and need_save_bitmap.IsOk():
            # dlg = wx.TextEntryDialog(self.GetParent(), "截图名称", "保存截图", value="202009071211001")
            # dlg.ShowModal()

            file_dlg = wx.FileDialog(self.GetParent(),
                                     message="截图保存",
                                     defaultDir=IMAGE_DIR,
                                     defaultFile=UtilityPanel.set_default_file_name(),
                                     wildcard="图片文件(*.jpg)|*.jpg|"
                                              "图片文件(*.png)|*.png|"
                                              "图标文件(*.ico)|*.ico|"
                                              "动态图(*.gif)|*.gif|"
                                              "图片文件(*.jpeg)|*.jpeg|"
                                              "所有文件(*.*)|*.*",
                                     style=wx.FC_SAVE,
                                     pos=wx.DefaultPosition)
            save_ok = file_dlg.ShowModal()
            if save_ok == wx.ID_OK:
                save_path = file_dlg.GetPath()
                save_file_name = file_dlg.GetFilename()
                print("path:", save_path)
                print("file name:", save_file_name)
                save = need_save_bitmap.SaveFile(save_path, type=wx.BITMAP_TYPE_JPEG)
                if save:
                    wx.MessageBox("保存截屏成功", "Save Image")
                else:
                    wx.MessageBox("保存截屏失败", "Error")
        else:
            wx.MessageBox("当前截屏为空", "Error")
            return

    @staticmethod
    def set_default_file_name():
        current_time_str = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        ram = random.randint(1, 999)
        if 10 <= ram < 100:
            ram_str = "0" + str(ram)
        elif 0 < ram < 10:
            ram_str = "00" + str(ram)
        else:
            ram_str = str(ram)
        default_file_name = current_time_str + ram_str
        return default_file_name





