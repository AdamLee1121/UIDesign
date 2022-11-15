# -*-coding: "utf-8"-*-

"""
# File:        COM_TEST.py
# Author:      "liyi"
# CreateTime:  2022/8/11 17:51
# Version:     python 3.6
# Description:   
"""
import win32com.client # the module needed for win32 COM API functions
import time
import os
import array
# -*- coding: utf-8 -*-

canape = win32com.client.Dispatch('CANape.Application')
print('\n')
print('CANape dispatched.')

#Init CANape
canape.Open1(r"D:\liyi10\project\VMM\ape_project\X02_NOA_Parking_0719_ModelReference",1,50000,True)
print('CANape initialized.')

# cfg_path = r"D:\liyi10\Downloads\X01_FSD_ACC_VMMSG_0627(1)\X01_FSD_ACC_VMMSG_0627\X01_FSD.cna"
# canape.LoadCNAFile(cfg_path)
# print('CANape initialized.')
# print("device number:", canape.Devices)

dev = canape.Devices.Add("NOA_CAL", r"VMM_main_Parking_20220424.a2l","XCP", 1)
print("device added")
print(canape.Devices.Count)
'''
try:
    calob1 = dev.CalibrationObjects.Item("1")
except:
    pass
'''


ca1 = "BSCL_PMS12State"
ca2 = "VehicleCtrlStateAp"
ca3 = "Park_CSMCtrlReq"
ca4 = "Park_AXCCtrlReq"
ca5 = "Park_VHCState"

dev.CalibrationObjects.Add("Out_VMM_LongMainAvailabilty")
calob = dev.CalibrationObjects.Item("Out_VMM_LongMainAvailabilty")

calob.Read()
Val = calob.Value
print("读取的数据：", Val)

# calob.Value = 1
# calob.write()
#
# time.sleep(3)
# calob.Read()
# Val = calob.Value
# print("观测前标定量写入后读取的数据：", Val)
#
# canape.Measurement.MDFFilename = "test.mdf"
# canape.Measurement.Start()
#
# time.sleep(5)
# run = canape.Measurement.Running
# print(run)
#
# time.sleep(5)
# calob.Value = 1
# calob.write()
# print("观测标定写入数据1:", calob.Value)
#
# time.sleep(5)
# calob.Value = 0
# calob.write()
# print("观测标定写入数据2:", calob.Value)
#
# time.sleep(5)
# calob.Value = 2
# calob.write()
# print("观测标定写入数据3：", calob.Value)
#
# time.sleep(10)
# print(canape.Measurement.MDFFilename)
# canape.Measurement.Stop()

print("pass")
