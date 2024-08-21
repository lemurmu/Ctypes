import time

import Net7668


def Example():
    print("QL7668.dll初始化...")
    Net7668.LoadNet7668Dll()

    ipstr = '127.0.0.1'
    ip = ipstr.encode("utf-8")
    port = 8080
    Net7668.ConnectByIp(ip, port)
    time.sleep(2)
    devId = Net7668.GetDeviceIdByIp(ip)
    if devId < 0:
        return
    isConnect = Net7668.GetConnectState(devId)
    if not isConnect:
        print("连接超时或设备未开启Socket！")
        return
    else:
        print("连接设备{0}成功!".format(devId + 1))
    newipStr = '192.168.10.125'
    maskStr = '255.255.255.255'
    defaultGatewayStr = '192.168.10.1'
    newip = newipStr.encode("utf-8")
    mask = maskStr.encode("utf-8")
    defaultGateway = defaultGatewayStr.encode("utf-8")
    Net7668.SetIp(devId, newip, mask, defaultGateway)

    # deviceNum = Net7668.ScanDevice()
    # if deviceNum <= 0:
    #     print("当前没有QL7668网络设备在线...")
    #     return
    # else:
    #     print("检测到有{0}个QL7668网络设备...".format(deviceNum))
    #
    # devices = []
    # for devId in range(0, deviceNum):
    #     deviceInfo = Net7668.GetDeviceByIndex(devId)
    #     name = str(deviceInfo.contents[0].name, 'utf-8')
    #     sn = str(deviceInfo.contents[0].sn, 'utf-8')
    #     version = str(deviceInfo.contents[0].version, 'utf-8')
    #     description = str(deviceInfo.contents[0].description, 'utf-8')
    #     ip_addr = str(deviceInfo.contents[0].ip_addr, 'utf-8')
    #     port = int.from_bytes(deviceInfo.contents[0].port, byteorder='little', signed=False)
    #     devices.append(deviceInfo)
    #     print("*******************设备{0}信息********************".format(devId + 1))
    #     print("设备名称:" + name)
    #     print("设备序列号:" + sn)
    #     print("设备版本:" + version)
    #     print("设备描述:" + description)
    #     print("设备ip地址:{0}:{1}".format(ip_addr, port))
    # print("************************************")
    #
    # devId = 0
    # Net7668.Connect(devId)
    # time.sleep(3)
    # isConnect = Net7668.GetConnectState(devId)
    # if not isConnect:
    #     print("连接超时或设备未开启Socket！")
    #     return
    # else:
    #     print("连接设备{0}成功!".format(devId + 1))
    # # 查询版本信息
    # hardwareVer = ctypes.create_string_buffer(15)
    # fpgaVer = ctypes.create_string_buffer(15)
    # embeddedVer = ctypes.create_string_buffer(18)
    # Net7668.Get_Version(devId, hardwareVer, fpgaVer, embeddedVer)
    # print("硬件版本信息:{0} FPGA版本信息:{1} 嵌入式版本信息:{2}".format(str(hardwareVer.value, "utf-8"), str(fpgaVer.value, "utf-8"),
    #                                                    str(embeddedVer.value, "utf-8")))
    # # 设置数据通道参数
    # dio_0_25_in_out = 0x03ffffff
    # dio_0_25_outmode = 0x03ffffff
    # sendMode = 0x00
    # Net7668.Set_DIO0_25_InOut(devId, dio_0_25_in_out, dio_0_25_outmode, sendMode)
    # # 数据通道参数查询
    # in_out = ctypes.c_int(0)
    # outmode = ctypes.c_int(0)
    # sendMode = ctypes.c_byte(0)
    # isComplete = ctypes.c_byte(0)
    # Net7668.Get_DIO0_25_InOut(devId, in_out, outmode, sendMode, isComplete)
    # print("数据通道参数:{0} {1} {2} {3}".format(hex(in_out.value), hex(outmode.value), sendMode.value, isComplete.value))
    # print("******************数据写入****************")
    #
    # # 写数据函数顺序:Set_DIO0_25_InOut->Set_Clock->Set_Pulse_Circle->Set_DIO26_29_InOut->Stop->Set_Data_Pulse_Deep->Write_Data_Pulse->Start
    # # 读数据函数顺序:Stop->Set_DIO0_25_InOut->Set_Clock->Set_Pulse_Circle->Set_DIO26_29_InOut->Start->Read_Data_Pulse，也可以直接Read_Data_Pulse
    # # 设置时钟通道参数
    # dio30_in_out = ctypes.c_byte(0x01)
    # dio31_in_out = ctypes.c_byte(0x01)
    # dio30_startLevel = ctypes.c_byte(0x00)
    # dio31_startLevel = ctypes.c_byte(0x00)
    # dio30_Edge = ctypes.c_byte(0x01)
    # dio31_Edge = ctypes.c_byte(0x00)
    # dio0_25_frequency = ctypes.c_double(10000.00)
    # dio26_29_frequency = ctypes.c_double(10000.00)
    # Net7668.Set_Clock(devId, dio30_in_out, dio31_in_out, dio30_startLevel, dio31_startLevel, dio30_Edge, dio31_Edge,
    #                   dio0_25_frequency, dio26_29_frequency)
    # # 设置脉冲占空比
    # dio26Cycle = ctypes.c_double(0.50)
    # dio27Cycle = ctypes.c_double(0.50)
    # dio28Cycle = ctypes.c_double(0.50)
    # dio29Cycle = ctypes.c_double(0.50)
    # frequency = ctypes.c_double(10000.00)
    # Net7668.Set_Pulse_Circle(devId, dio26Cycle, dio27Cycle, dio28Cycle, dio29Cycle, frequency)
    #
    # # 设置脉冲通道参数
    # # 四个通道都输出
    # in_out = ctypes.c_byte(0x0F)
    # # 都输出脉冲
    # outmode = ctypes.c_byte(0x00)
    # # 都起始电平为高电平
    # startLevel = ctypes.c_byte(0x0F)
    # # 发送模式设置为循环发送
    # sendMode = ctypes.c_byte(0x01)
    # Net7668.Set_DIO26_29_InOut(devId, in_out, outmode, startLevel, sendMode)
    #
    # Net7668.Stop(devId)
    # xx = 0x3fffffff
    # deep = 256
    # data = (ctypes.c_int * deep)()
    # for n in range(0, deep):
    #     data[n] = xx
    # # 设置数据脉冲深度
    # level = 0x0a
    # Net7668.Set_Data_Pulse_Deep(devId, deep, deep, level)
    # # 写入数据
    # Net7668.Write_Data_Pulse(devId, data, deep)
    # Net7668.Start(devId)
    # # 读取数据
    # readLen = 200
    # recvData = (ctypes.c_int * readLen)()
    # for r in range(0, readLen):
    #     recvData[r] = 0
    # Net7668.Read_Data_Pulse(devId, recvData, readLen)
    # recvStr = ""
    # for r in range(0, readLen):
    #     recvStr += hex(recvData[r]) + "-"
    # print("读取脉冲数据:{0}".format(recvStr))

    print("释放QL7668.dll资源...")
    Net7668.UnLoadNet7668Dll()


if __name__ == '__main__':
    Example()
