import Gui
import unittest
import requests
import json
import re

class CGI(unittest.TestCase):
    MACAddress = ''  # MACAddress值

    def test_AllCgi(self):
        # 启动输入配置数据的弹窗
        # Gui.ConfigData.message(self)

        # 调用获取当前IP地址设备的MAC地址方法
        CGI.getMACAddress(Gui.ConfigData)

    # 获取设备的MAC地址
    def getMACAddress(self):
        # 封装CGI url请求地址
        # url = "http://" + self.ipcUrl +"/cgi-bin/param.cgi?userName=" + self.username + "&password=" + self.password + "&action= get&type=deviceInfo"
        url = "http://192.168.1.65/cgi-bin/param.cgi?userName=admin&password=admin&action=get&type=deviceInfo"
        # 调用CGI，处理返回字符串，获取MAC地址
        CGI.MACAddress = requests.get(url).text.split('\r\n')[6].split('=')[1]


        # 有空优化成对象




if __name__ == '__main__':
    unittest.main()
