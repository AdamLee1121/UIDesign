# Standard library imports
import os
import sys
import time
import msvcrt
from win32com.client import *
from win32com.client.connect import *


# Vector Canoe Class
class CANoe:
    def __init__(self):
        self.application = None
        self.application = Dispatch("CANoe.Application")
        self.ver = self.application.Version
        print('Loaded CANoe version ',
              self.ver.major, '.',
              self.ver.minor, '.',
              self.ver.Build, '...')  # , sep,''
        self.Measurement = self.application.Measurement.Running

    def cfg_open(self, cfgname):
        if(self.application != None):
            if os.path.isfile(cfgname) and (os.path.splitext(cfgname)[1]==".cfg"):
                self.application.Open(cfgname)
                print("openning..." + cfgname)
            else:
                raise RuntimeError("Can't find CANoe cfg file!")
        else:
            raise RuntimeError("CANoe Application is missing, unable to simulate!")

    def cfg_close(self):
        if(self.application):
            self.application.Quit()
            self.application = None
            print("CANoe Application is closed!")

    def start_Measurement(self):
        retry = 0
        retry_counter = 5
        # 给出5s延时检查，保证测量开始的状态下进行后续操作
        while not self.application.Measurement.Running and (retry < retry_counter):
            self.application.Measurement.Start()
            time.sleep(1)
            retry += 1
        if retry == retry_counter:
            raise RuntimeError("CANoe start measurement failed, please check connection!")

    def stop_Measurement(self):
        if self.application.Measurement.Running:
            self.application.Measurement.Stop()
        else:
            pass

    def get_nodes(self):
        if self.application:
            return self.application.Configuration.SimulationSetup.Buses

    # 数据交互、读写信号
    def get_sigVal(self, channel_num, msg_name, sig_name, bus_type="CAN"):
        if self.application:
            result = self.application.GetBus(bus_type).GetSignal(channel_num, msg_name, sig_name)
            # print(result.FullName, '\n', result.RawValue)
            return result.Value
        else:
            raise RuntimeError("CANoe is not open, unable to GetVariable!")

    def set_sigVal(self, channel_num, msg_name, sig_name, setVal, bus_type="CAN"):
        if self.application:
            # bus_type = "CAN"
            result = self.application.GetBus(bus_type).GetSignal(channel_num, msg_name, sig_name)
            result.Value = setVal
            # print("设置成功", result)
        else:
            raise RuntimeError("CANoe is not open, unable to GetVariable!")

    def get_Envar(self, var):
        """
        获取环境变量的数值
        :param var:
        :return:
        """
        if (self.application != None):
            result = self.application.Environment.GetVariable(var)
            return result.Value

    def set_Envar(self, var, value):
        """
        为环境变量赋值
        :param var:
        :param value:
        :return:
        """
        result = None
        if(self.application != None):
            result = self.application.Environment.GetVariable(var)
            result.Value = value
            checker = self.get_Envar(var)

            while(checker != value):
                checker = self.get_Envar(var)

    def get_mes(self, channel_num, msg_name):
        result = self.application.GetBus("CAN").GetMessage(channel_num, msg_name)
        return result

    # 阻塞进程
    def DoEvents(self, cycle_time):
        pythoncom.PumpWaitingMessages()
        time.sleep(cycle_time)


# app = CANoe()
# # app = Dispatch("CANoe.Application")  # 实例化对象
# # app.cfg_open(r'C:\Users\Public\Documents\Vector\CANoe\Sample Configurations 12.0.75\Programming\Python\CANoeConfig\PythonBasic.cfg')
# # app.cfg_open(r"D:/liyi10/Downloads/CANoe/VMM/CANoe10-VMM.cfg")
#
# # app.cfg_open(r'C:\Users\Public\Documents\Vector\CANoe\Sample Configurations 12.0.75\Programming\Python\CANoeConfig\PythonBasicEmpty.cfg')
#
# app.cfg_open(r"D:/liyi10/Downloads/CANoe/VMM/CANoe10-VMM.cfg")
# # time.sleep(10)
# # nodes = app.get_nodes()
# app.start_Measurement()
# while not msvcrt.kbhit():
#     # app.set_sigVal(1, "ASU_Info1_10ms", "SusHghtLvlSnsrRR", 1)
#     app.set_sigVal(1, "XCU_Info_10ms_FD", "AccelPdlPos", 9)
#     app.set_sigVal(2, "XCU_Info_10ms_FD", "AccelPdlPos", 1)
#     # app.set_sigVal(1, "SP1_Info1_10ms", "ADAS_FaultStatus", 2)
#     # app.DoEvents()
#     # AccelPos = app.get_sigVal(1, "XCU_Info_10ms_FD", "AccelPdlPos")
#     # print(AccelPos)
#     # EngineSpeed = app.get_sigVal(channel_num=1, msg_name="EngineState", sig_name="EngineSpeed", bus_type="CAN")
#     # app.set_sigVal(channel_num=1, msg_name="EngineState", sig_name="EngineSpeed", setVal=2.0, bus_type="CAN")
#     app.DoEvents(0.01)
# i = 0
# while i<10000:
#     app.set_sigVal(1, "XCU_Info_10ms_FD", "AccelPdlPos", 3)
#     i+=1
# app.get_sigVal(1, "XCU_Info_10ms_FD", "AccelPdlPos")

# app.start_Measurement()
# time.sleep(5)
# app.stop_Measurement()
# time.sleep(10)
# app.cfg_close()
# app.getSignal()
# print(app.get_nodes())
#
# while not msvcrt.kbhit():
#     EngineSpeed = app.get_sigVal(channel_num=1, msg_name="EngineState", sig_name="EngineSpeed", bus_type="CAN")
#     app.set_sigVal(channel_num=1, msg_name="EngineState", sig_name="EngineSpeed",setVal=2.0, bus_type="CAN")
#     print(EngineSpeed)
#     app.DoEvents()





