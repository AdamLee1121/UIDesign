

import sys
from uiClass import testTool
from PyQt5.QtWidgets import QApplication, QWidget

# Press the green button in the gutter to run the script.
# import openpyxl
#
# wb = openpyxl.load_workbook("mapping_testcase.xlsx")
# print(wb.sheetnames)
# sheet_data = wb.get_sheet_by_name("CANRx")
# # sheet_data = wb['CANRx']
#
# for i in range(3, sheet_data.max_row+1):
#     # sheet_data.cell(i,3).value = sheet_data.cell(i,3).value+"=1"
#     if sheet_data.cell(i,5).value == "未找到" or not sheet_data.cell(i,5).value:
#         sheet_data.delete_rows(i)
#     else:
#         sheet_data.cell(i, 5).value = sheet_data.cell(i, 5).value + "=1"
#
# wb.save("mapping_testcase4.xlsx")

from canoeClass import canoe
from canapeClass import canape
import time

oe = canoe.CANoe()
oe.cfg_open(r"D:/liyi10/Downloads/CANoe/VMM/CANoe10-VMM.cfg")

ape = canape.CANape()
ape.initial(r"D:\liyi10\project\VMM\ape_project\X02_NOA_Parking_0719_ModelReference","NOA_CAL","VMM_main_Parking_20220424.a2l")
print('ape initialized.')
"""
# case1
mdfname1 = "Autotest" + time.strftime('%Y-%m-%d-%H-%M-%S')
ape.application.Measurement.MDFFilename = mdfname1

oe.start_Measurement()
ape.measurement_start()
oe.set_Envar("env_gear",1)
time.sleep(10)

ape.calibration_by_name("P_HAP_StopDistance", 800)
time.sleep(5)
ape.calibration_by_name("P_HAP_StopDistance", 0)
oe.set_Envar("env_whlspd_value",5)
oe.set_Envar("env_whlspd_ena",1)
time.sleep(10)

oe.stop_Measurement()
ape.measurement_stop()
# time.sleep(10)
"""
# ---------------------------------------
# case2
mdfname2 = "Autotest" + time.strftime("%Y-%m-%d-%H-%M-%S")
ape.application.Measurement.MDFFilename = mdfname2

oe.start_Measurement()
ape.measurement_start()
ape.calibration_by_name("P_HAP_StopDistance", 800)
oe.set_Envar("env_gear",3)
oe.set_Envar("env_whlspd_value", 0.3)
oe.set_Envar("env_whlspd_ena", 1)
time.sleep(10)

oe.set_Envar("env_whldirection", 2)
oe.set_Envar("env_whlspd_value", 5)
time.sleep(10)
oe.set_Envar("env_whlspd_value", 0.2)
time.sleep(5)
oe.set_Envar("env_whlspd_value", 0)
time.sleep(5)
oe.set_Envar("env_whldirection", 0)
time.sleep(5)

ape.measurement_stop()
oe.stop_Measurement()