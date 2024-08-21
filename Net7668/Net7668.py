# -*- coding: utf-8 -*-
# @Time    : 2023/8/9 14:37
# @Author  : yzc
# @File    : Net7668.py
# @Description :Net7668 API接口

import ctypes

global handle


# 定义设备信息结构体
class DeviceInfo(ctypes.Structure):
    _fields_ = (
        ('name', ctypes.c_char * 10),
        ('sn', ctypes.c_char * 30),
        ('version', ctypes.c_char * 10),
        ('description', ctypes.c_char * 32),
        ('ip_addr', ctypes.c_char * 32),
        ('port', ctypes.c_char * 4),
    )


def LoadNet7668Dll():
    """
    加载Net7668动态库并初始化
    :return:
    """
    global handle
    handle = ctypes.cdll.LoadLibrary("./Net7668.dll")
    handle.LoadDevice()


def UnLoadNet7668Dll():
    """
    关闭Net7668动态库并释放资源
    :return:
    """
    global handle
    handle.CloseDevice()


def ScanDevice():
    """
    扫描局域网内的所有QL7668设备
    :return:
    """
    global handle
    num = handle.ScanDevice()
    return num


def GetDeviceByIndex(devid):
    """
    通道设备ID获取设备信息
    :param devid:设备id，id号为0~（ScanDevice扫描的设备数量-1）
    :return:设备信息结构体
    """
    global handle

    handle.GetDeviceByIndex.restype = ctypes.POINTER(DeviceInfo * 1)
    deviceInfo = handle.GetDeviceByIndex(devid)
    return deviceInfo


def Connect(devid):
    """
    异步连接设备
    :param devid:
    :return:函数执行结果
    """
    global handle
    return handle.Connect(devid)


def ConnectByIp(ip, port):
    """
    通过ip连接设备
    :param ip:
    :param port:
    :return:
    """
    global handle
    # handle.ConnectByIp.argtypes = [ctypes.c_wchar_p, ctypes.c_int]
    return handle.ConnectByIp(ip, port)


def GetDeviceIdByIp(ip):
    """
    通过ip获取设备id
    :param ip:
    :return:
    """
    global handle
    return handle.GetDeviceIdByIp(ip)


def GetConnectState(devid):
    """
    获取连接状态
    :param devid:
    :return:
    """
    global handle
    return handle.GetConnectState(devid)


def Get_Version(devid, hardwareVer, fpgaVer, embeddedVer):
    """
    获取FPGA和嵌入式版本信息
    :param devid:设备id
    :param hardwareVer:硬件版本
    :param fpgaVer:fpga版本
    :param embeddedVer:嵌入式版本
    :return:
    """
    global handle
    handle.Get_Version.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
    handle.Get_Version(devid, hardwareVer, fpgaVer, embeddedVer)


def Set_DIO0_25_InOut(devid, in_out, outmode, sendMode):
    """
    设置数据通道参数
    :param devid:设备id
    :param in_out:data[25:0]表示26个DIO的输入输出 0：输入 1：输出
    :param outmode:data[25:0]表示26个DIO的输入输出模式，0:输出数据 1：输出时钟
    :param sendMode:发送模式0x00: Burst模式,单次发；0x01: Continuous模式，循环发送
    :return:
    """
    global handle
    handle.Set_DIO0_25_InOut.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_byte]
    return handle.Set_DIO0_25_InOut(devid, in_out, outmode, sendMode)


def Get_DIO0_25_InOut(devid, in_out, outmode, sendMode, isComplete):
    """
    获取数据通道参数
    :param devid: 设备id
    :param in_out: data[25:0]表示26个DIO的输入输出 0：输入 1：输出
    :param outmode:data[25:0]表示26个DIO的输入输出模式，0:输出数据 1：输出时钟
    :param sendMode: 发送模式0x00: Burst模式,单次发；0x01: Continuous模式，循环发送
    :param isComplete: 是否完成
    :return:
    """
    global handle
    handle.Get_DIO0_25_InOut(devid, ctypes.byref(in_out), ctypes.byref(outmode), ctypes.byref(sendMode),
                             ctypes.byref(isComplete))


def Set_Data_Pulse_Deep(devid, dataChannelDeep, pulseChannelDeep, level):
    """
    设置数据脉冲深度
    :param devid: 设备id
    :param dataChannelDeep: 数据通道数据深度
    :param pulseChannelDeep: 脉冲通道数据深度
    :param level: 接口电平 0x00:表示关闭接口电源 0x0a:表示设置接口LVCMOS18，0x09:表示设置接口LVCMOS25，0x0c:表示设置接口LVCMOS33，0x0d:表示设置接口5VTTL。
    :return:
    """
    global handle
    handle.Set_Data_Pulse_Deep.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_byte]
    return handle.Set_Data_Pulse_Deep(devid, dataChannelDeep, pulseChannelDeep, level)


def Get_Data_Pulse_Deep(devid, dataChannelDeep, pulseChannelDeep, level):
    """
    获取数据脉冲深度
    :param devid: 设备id
    :param dataChannelDeep: 数据通道深度
    :param pulseChannelDeep: 脉冲通道参数
    :param level: 接口电平
    :return:
    """
    global handle
    handle.Get_Data_Pulse_Deep(devid, ctypes.byref(dataChannelDeep), ctypes.byref(pulseChannelDeep),
                               ctypes.byref(level))


def Write_Data_Pulse(devid, data, length):
    """
    写入数据脉冲
    :param devid:设备id
    :param data: d29-d0:一个int表示30个通道的数据 小端模式
    :param length:数据长度 多少个int数据
    :return:
    """
    global handle
    return handle.Write_Data_Pulse(devid, data, length)


def Read_Data_Pulse(devid, dio0_dio29, readLen):
    """
    读取数据脉冲
    :param devid:设备id
    :param dio0_dio29: d29-d0:一个int表示30个通道的数据 小端模式
    :param readLen:数据长度 多少个int数据
    :return:
    """
    global handle
    handle.Read_Data_Pulse(devid, dio0_dio29, readLen)


def Set_DIO26_29_InOut(devid, in_out, outmode, startLevel, sendMode):
    """
    设置脉冲通道参数
    :param devid:设备id
    :param in_out:data[3:0] 表示dio29-dio26的输入输出
    :param outmode:data[3:0] 表示dio29-dio26的输出模式
    :param startLevel:data[3:0] 表示dio29-dio26的起始电平 0：低电平 1高电平
    :param sendMode:发送模式 0x00: Burst模式,单次发；0x01: Continuous模式，循环发送
    :return:
    """
    global handle
    handle.Set_DIO26_29_InOut.argtypes = [ctypes.c_int, ctypes.c_byte, ctypes.c_byte, ctypes.c_byte, ctypes.c_byte]
    return handle.Set_DIO26_29_InOut(devid, in_out, outmode, startLevel, sendMode)


def Get_DIO26_29_InOut(devid, in_out, outmode, startLevel, sendMode, isStart):
    """
    获取脉冲通道的参数
    :param devid: 设备id
    :param in_out: data[3:0] 表示dio29-dio26的输入输出
    :param outmode: data[3:0] 表示dio29-dio26的输出模式
    :param startLevel: data[3:0] 表示dio29-dio26的起始电平 0：低电平 1高电平
    :param sendMode: sendMode:发送模式 0x00: Burst模式,单次发；0x01: Continuous模式，循环发送
    :param isStart: 是否启动
    :return:
    """
    global handle
    handle.Get_DIO26_29_InOut(devid, ctypes.byref(in_out), ctypes.byref(outmode), ctypes.byref(startLevel),
                              ctypes.byref(sendMode), ctypes.byref(isStart))


def Start(devid):
    """
    启动
    :param devid:
    :return:
    """
    global handle
    return handle.Start(devid)


def Stop(devid):
    """
    停止
    :param devid:
    :return:
    """
    global handle
    return handle.Stop(devid)


def Set_Pulse_Circle(devid, dio26Cycle, dio27Cycle, dio28Cycle, dio29Cycle, frequency):
    """
    设置脉冲占空比
    :param devid:设备id
    :param dio26Cycle:占空比
    :param dio27Cycle:占空比
    :param dio28Cycle:占空比
    :param dio29Cycle:占空比
    :param frequency:脉冲通道频率 ch31的频率
    :return:
    """
    global handle
    return handle.Set_Pulse_Circle(devid, dio26Cycle, dio27Cycle, dio28Cycle, dio29Cycle, frequency)


def Get_Pulse_Circle(devid, dio26Cycle, dio27Cycle, dio28Cycle, dio29Cycle, frequency):
    """
    读取脉冲占空比
    :param devid:设备id
    :param dio26Cycle:占空比
    :param dio27Cycle:占空比
    :param dio28Cycle:占空比
    :param dio29Cycle:占空比
    :param frequency:脉冲通道频率 ch31的频率
    :return:
    """
    global handle
    handle.Get_Pulse_Circle(devid, ctypes.byref(dio26Cycle), ctypes.byref(dio27Cycle), ctypes.byref(dio28Cycle),
                            ctypes.byref(dio29Cycle), frequency)


def Set_Clock(devid, dio30_in_out, dio31_in_out, dio30_startLevel, dio31_startLevel, dio30_Edge, dio31_Edge,
              dio0_25_frequency, dio26_29_frequency):
    """
    时钟设置
    :param devid: 设备id
    :param dio30_in_out: ch30输入输出 0：输入 1：输出
    :param dio31_in_out: ch31输入输出 0：输入 1：输出
    :param dio30_startLevel: ch30起始电平 0：低电平 1：高电平
    :param dio31_startLevel: ch31起始电平 0：低电平 1：高电平
    :param dio30_Edge: ch30接收边沿 0：下降沿 1：上升沿
    :param dio31_Edge: ch31接收边沿 0：下降沿 1：上升沿
    :param dio0_25_frequency:ch30时钟频率
    :param dio26_29_frequency:ch31时钟频率
    :return:
    """
    global handle
    return handle.Set_Clock(devid, dio30_in_out, dio31_in_out, dio30_startLevel, dio31_startLevel, dio30_Edge,
                            dio31_Edge,
                            dio0_25_frequency, dio26_29_frequency)


def Get_Clock(devid, dio30_in_out, dio31_in_out, dio30_startLevel, dio31_startLevel, dio30_Edge, dio31_Edge,
              dio0_25_frequency, dio26_29_frequency):
    """
    时钟读取
    :param devid: 设备id
    :param dio30_in_out: ch30输入输出 0：输入 1：输出
    :param dio31_in_out: ch31输入输出 0：输入 1：输出
    :param dio30_startLevel: ch30起始电平 0：低电平 1：高电平
    :param dio31_startLevel: ch31起始电平 0：低电平 1：高电平
    :param dio30_Edge: ch30接收边沿 0：下降沿 1：上升沿
    :param dio31_Edge: ch31接收边沿 0：下降沿 1：上升沿
    :param dio0_25_frequency:ch30时钟频率
    :param dio26_29_frequency:ch31时钟频率
    :return:
    """
    global handle
    handle.Get_Clock(devid, ctypes.byref(dio30_in_out), ctypes.byref(dio31_in_out), ctypes.byref(
        dio30_startLevel), ctypes.byref(dio31_startLevel), ctypes.byref(dio30_Edge),
                     ctypes.byref(dio31_Edge),
                     ctypes.byref(dio0_25_frequency), ctypes.byref(dio26_29_frequency))


def SetIp(devid, ipaddr, mask, defaultGateway):
    """
    设置ip地址
    :param devid:
    :param ipaddr:
    :param mask:
    :param defaultGateway:
    :return:
    """
    global handle
    handle.Set_Ipv4(devid, ipaddr, mask, defaultGateway)
