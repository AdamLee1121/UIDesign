# -*-coding: "utf-8"-*-

"""
# File:        ape_test.py
# Author:      "liyi"
# CreateTime:  2022/7/18 14:54
# Version:     python 3.6
# Description:   
"""
from win32com.client import *
from win32com.client.connect import *
import time
import ctypes
from enum import IntEnum, Enum

"""
class CANape():
    def __init__(self):
        self._stateActive = self.ifActive()
        self._apeApp = DispatchEx("CANape.Application")
        self._recorder = self.recorder()

    def open_cfg(self, cfgpath: str=None):
        if not cfgpath:
            self._apeApp.Open1(cfgpath, 1, 1000, 1)
            devices = self._apeApp.Devices.Item()

    def start_measurement(self, cfgpath: str = None):
        try:
            self._apeApp.Opne1(cfgpath, 1, 1000, 1)
            # 未编写完成
            # 开始之前，需要先添加device，go online
            self._apeApp.Measurement.Start()
        except

    def stop_measurement(self):
        self._apeApp.Measurement.Stop()

    def recorder(self):
        return self._apeApp.Recorders.Add(f"Recorder_{time.strftime('%Y-%m-%d-%H-%M', time.localtime())}")

    def ifActive(self):
        return True if self._apeApp is not None else False
"""
"""
# 连上所有硬件后执行这段代码，查看是否可以自动查询到devices
apeCom = DispatchEx("CANape.Application")

# try:
#     apeCom.Open1(r"D:\liyi10\Downloads\X01_FSD_ACC_VMMSG_0627(1)\X01_FSD_ACC_VMMSG_0627", 1, 1000, 1) #(1)\X01_FSD_ACC_VMMSG_0627
# except:
#     pass
# xcp = apeCom.Devices.Item(0)
# xcp_download = xcp.Download(r"VMM_main_Updated.a2l")
# xcp.GoOnline(xcp_download)

# recorder = apeCom.Recorders.Add(f"Recorder_{time.strftime('%Y-%m-%d-%H-%M', time.localtime())}")
# print(recorder.Name)

# recorder.MDFFilename = recorder.Name

a2l = r"D:\liyi10\Downloads\X01_FSD_ACC_VMMSG_0627(1)\X01_FSD_ACC_VMMSG_0627\liauto_x01_fsd_mcu_A_f106 (1)\X01-FSD-MCU1-f106\VMM_main_Updated.a2l"
# cfg_path = r"D:\liyi10\Downloads\X01_FSD_ACC_VMMSG_0627(1)\X01_FSD_ACC_VMMSG_0627\liauto_x01_fsd_mcu_A_f106 (1)\X01-FSD-MCU1-f106\X01_FSD.cna"
cfg_path = r"D:\liyi10\Downloads\X01_FSD_ACC_VMMSG_0627\X01_FSD.cna"
apeCom.LoadCNAFile(cfg_path)
"""
"""
# 添加device
xcp_device = apeCom.Devices.Add2("NOA_CAL", a2l, "XCP", 1, False)
# print(apeCom.Devices.Count)
# print(apeCom.Exception.ErrorText)
print(xcp_device.Databases.Count)
# 添加网络
Eth = apeCom.NetWorks
print(apeCom.NetWorks.Count)



# 设备在线
# if not xcp_device.IsOnline:
#     xcp_device.GoOnline(False)

# xcp_device.ReadMemory(addr: long, size: long) 可以根据地址直接读取内存

# 设置标定量
# cal_sig_name = "P_AXC_ClsdLoopCtrlUpSpdThd"
# cal_obj = xcp_device.CalibrationObjects.Add2(cal_sig_name)

# 在线标定
# cal_obj.Value = 0.2
# cal_obj.Write()

# 启动measure
# xcp_device

# time.sleep(5)
# apeCom.Measurement.Start()
"""

# *****************************************调用dll*************************************

header_file = r"D:\liyi10\software\CANape\CANapeAPI\CANapAPI.h"
CANapAPI_dll = r"D:\liyi10\software\CANape\CANapeAPI\CANapAPI64.dll"


def first_occurance(needle):
    with open(header_file, "r") as haystack:
        for line_no, line in enumerate(haystack.readlines()):
            if needle in line:
                print(f"'{needle}' first occurs on line {line_no} in {header_file}")
                return


class struct_tAsap3Hdl(ctypes.Structure):
    pass


class ushort_tModulHdl(ctypes.c_ushort):
    pass


class value(ctypes.Structure):
    pass
    # def __init__(self):
    #     self.type = TValueType.VALUE
    #     self.value = ctypes.c_double(0)
value._fields_ = [
    ("type", ctypes.c_int),
    ("value", ctypes.c_double)
]


class axis(ctypes.Structure):
    pass
    # def __init__(self):
    #     self.type = TValueType.AXIS
    #     self.dimension = ctypes.c_short(0)
    #     self.axis = ctypes.POINTER(ctypes.c_double)


axis._fields_ = [
    ("type", ctypes.c_int),
    ("dimension", ctypes.c_short),
    ("axis", ctypes.POINTER(ctypes.c_double))
]


class ascii(ctypes.Structure):
    # def __init__(self):
    #     self.type = TValueType.ASCII
    #     self.len = ctypes.c_short(0)
    #     self.ascii = ctypes.c_char_p()
    pass


ascii._fields_ = [
    ("type", ctypes.c_int),
    ("len", ctypes.c_short),
    ("ascii", ctypes.c_char_p)
]


class curve(ctypes.Structure):
    # def __init__(self):
    #     self.type = TValueType.CURVE
    #     self.axis = ctypes.POINTER(ctypes.c_double)
    #     self.values = ctypes.POINTER(ctypes.c_double)
    pass


curve._fields_ = [
    ("type", ctypes.c_int),
    ("dimension", ctypes.c_short),
    ("axis", ctypes.POINTER(ctypes.c_double)),
    ("values", ctypes.POINTER(ctypes.c_double))
]


class map(ctypes.Structure):
    # def __init__(self):
    #     self.type = TValueType.MAP
    #     self.xDimension = 0
    #     self.yDimension = 0
    #     self.xAxis = ctypes.POINTER(ctypes.c_double)
    #     self.yAxis = ctypes.POINTER(ctypes.c_double)
    #     self.values = ctypes.POINTER(ctypes.c_double)
    pass


map._fields_ = [
    ("type", ctypes.c_int),
    ("xDimension", ctypes.c_short),
    ("yDimension", ctypes.c_short),
    ("xAxis", ctypes.POINTER(ctypes.c_double)),
    ("yAxis", ctypes.POINTER(ctypes.c_double)),
    ("values", ctypes.POINTER(ctypes.c_double))
]


class valblk(ctypes.Structure):
    # def __init__(self):
    #     self.type = TValueType.VAL_BLK
    #     self.xDimension = 0
    #     self.yDimension = 0
    #     self.values = ctypes.POINTER(ctypes.c_double)
    pass


valblk._fields_ = [
    ("type", ctypes.c_int),
    ("xDimension", ctypes.c_short),
    ("yDimension", ctypes.c_short),
    ("values", ctypes.POINTER(ctypes.c_double))
]


class TCalibrationObjectValue(ctypes.Union):
    # def __init__(self):
    #     self.type = TValueType.VALUE
    #     self.value = value()
    #     self.axis = axis()
    #     self.ascii = ascii()
    #     self.curve = curve()
    #     self.map = map()
    #     self.valblk = valblk()
    _fields_ = [
        ("type", ctypes.c_int),
        ("value", value),
        ("axis", axis),
        ("ascii", ascii),
        ("curve", curve),
        ("map", map),
        ("valblk", valblk),
    ]


class TTaskInfo(ctypes.Structure):
    # def __init__(self):
    #     self. description = ctypes.c_char_p
    #     self.taskId = ctypes.c_ushort
    #     self.taskCycle = ctypes.c_ushort
    pass


TTaskInfo._fields_ = [
    ("description", ctypes.c_char_p),
    ("taskId", ctypes.c_ushort),
    ("taskCycle", ctypes.c_ushort)
]

class Appversion(ctypes.Structure):
    pass
Appversion._fields_ = [
    ("MainVersion", ctypes.c_int),
    ("SubVersion", ctypes.c_int),
    ("ServecePack", ctypes.c_int),
    ("Application", ctypes.c_char),
]

dll = ctypes.windll.LoadLibrary(CANapAPI_dll)

# 之后参数hdl均用此句柄
TAsap3Hdl = ctypes.POINTER(struct_tAsap3Hdl)
handle = TAsap3Hdl()
handle_p = ctypes.byref(handle)

TModulHdl = ctypes.c_ushort()
handle_p_m = ctypes.byref(TModulHdl)


# -------------------------枚举---------------------
class TFormat(IntEnum):
    ECU_INTERNAL = 0
    PHYSICAL_REPRESENTATION = 1


class TValueType(IntEnum):
    VALUE = 0
    CURVE = 1
    MAP = 2
    AXIS = 3
    ASCII = 4
    VAL_BLK = 5


# ----------------打开canape---------------------
workingDir = r"D:\liyi10\Downloads\X01_FSD_ACC_VMMSG_0627(1)\X01_FSD_ACC_VMMSG_0627"
responseTimeout = 120000
fifoSize = 2048#8192
sampleSize = 1024#256
debugMode = True
clearDeviceList = False
bHexmode = False
bModalMode = False

c_responseTimeout = ctypes.c_ulong(responseTimeout)
c_workingDir = ctypes.c_char_p(workingDir.encode("UTF-8"))
c_fifoSize = ctypes.c_ulong(fifoSize)
c_sampleSize = ctypes.c_ulong(sampleSize)
c_debugMode = ctypes.c_bool(debugMode)
c_clearDeviceList = ctypes.c_bool(clearDeviceList)
c_bHexmode = ctypes.c_bool(bHexmode)
c_bModalMode = ctypes.c_bool(bModalMode)

first_occurance("Asap3Init5")

dll.Asap3Init5.restype = ctypes.c_bool
dll.Asap3Init5.argtypes = (
    ctypes.POINTER(TAsap3Hdl),
    ctypes.c_ulong,
    ctypes.c_char_p,
    ctypes.c_ulong,
    ctypes.c_ulong,
    ctypes.c_bool,
    ctypes.c_bool,
    ctypes.c_bool,
    ctypes.c_bool
)
apeApp = dll.Asap3Init5(
    handle_p,
    c_responseTimeout,
    c_workingDir,
    c_fifoSize,
    c_sampleSize,
    c_debugMode,
    c_clearDeviceList,
    c_bHexmode,
    c_bModalMode,
)
print(apeApp)
# ----------------------------加载工程------------------------------------
first_occurance("Asap3LoadCNAFile")

configFileName = "X01_FSD.cna"
c_configFileName = ctypes.c_char_p(configFileName.encode("UTF-8"))

dll.Asap3LoadCNAFile.restype = ctypes.c_bool
dll.Asap3LoadCNAFile.argtypes = (
    # ctypes.POINTER(struct_tAsap3Hdl),
    TAsap3Hdl,
    ctypes.c_char_p,
)

project = dll.Asap3LoadCNAFile(
    handle,
    c_configFileName,
)
"""
# -------------------------获取CANape版本----------------------------------
first_occurance("Asap3GetApplicationVersion")

appversion = Appversion()
c_appversion = ctypes.byref(appversion)
dll.Asap3GetApplicationVersion.restype = ctypes.c_bool
dll.Asap3GetApplicationVersion.argtypes = [
    TAsap3Hdl,
    ctypes.POINTER(Appversion),
]
result_version = dll.Asap3GetApplicationVersion(
    handle,
    c_appversion,
)

print("版本号:",result_version,'\n',appversion.Application,'---', appversion.MainVersion)
# -------------------------------------------------------------
"""
"""
# -------------------------检查工程内部设置----------------------------------
first_occurance("Asap3GetModuleCount")

count = 10
c_count = ctypes.c_ulong(count)
c_count_p = ctypes.byref(c_count)
dll.Asap3GetModuleCount.restype = ctypes.c_bool
dll.Asap3GetModuleCount.argtypes = (
    TAsap3Hdl,
    ctypes.POINTER(ctypes.c_ulong),
)
device_count_result = dll.Asap3GetModuleCount(
    handle,
    c_count_p,
)
print("查询设备数量结果", device_count_result)
print("设备数量", c_count.value)
# first_occurance("Asap3ECUOnOffline")
# -----------------------------------------------------------------------
"""
# ----------------------------获取active device----------------------------

first_occurance("Asap3IsModuleActive")

device_act = False
c_device_act = ctypes.c_bool(device_act)
c_device_act_p = ctypes.byref(c_device_act)
dll.Asap3IsModuleActive.restype = ctypes.c_bool
dll.Asap3IsModuleActive.argtypes = (
    TAsap3Hdl,
    ctypes.c_ushort,
    ctypes.POINTER(ctypes.c_bool)
)

active_module = dll.Asap3IsModuleActive(
    handle,
    TModulHdl,
    c_device_act_p,
)

# print(active_module)
# print(c_device_act.value)
# print(TModulHdl.value)
# ------------------------------------------------

"""
# -----新建设备-----
first_occurance("Asap3CreateModule")

moduleName = r"test"
databaseFilename = r"VMM_main_Updated.a2l"
driverType = 3
channelNo = 1

c_moduleName = ctypes.c_char_p(moduleName.encode("UTF-8"))
c_databaseFilename = ctypes.c_char_p(databaseFilename.encode("UTF-8"))
c_driverType = ctypes.c_short(driverType)
c_channelNo = ctypes.c_short(channelNo)
# print(c_moduleName,c_databaseFilename,c_driverType,c_channelNo)


dll.Asap3CreateModule.restype = ctypes.c_bool
dll.Asap3CreateModule.argtypes = (
    TAsap3Hdl,
    ctypes.c_char_p,
    ctypes.c_char_p,
    ctypes.c_short,
    ctypes.c_short,
    ctypes.POINTER(ctypes.c_ushort),
)

result = dll.Asap3CreateModule(
    handle,
    c_moduleName,
    c_databaseFilename,
    c_driverType,
    c_channelNo,
    handle_p_m,
)

print(result)
print(TModulHdl.value)
# -------------------------------------------------------------------------
"""
"""
# --------------------------------切换ROM RAM------------------------------------
time.sleep(10)
class Mode(IntEnum):
    e_TR_MODE_RAM = 0
    e_TR_MODE_ROM = 1

mode = Mode.e_TR_MODE_ROM
c_mode = ctypes.c_int(mode)

result_change1 = dll.Asap3SwitchToMemoryPage(handle, TModulHdl, c_mode)
print("result_change:",'\n', result_change1)

mode = Mode.e_TR_MODE_RAM
c_mode = ctypes.c_int(mode)

result_change2 = dll.Asap3SwitchToMemoryPage(handle, TModulHdl, c_mode)
# print("result_change:",'\n', result_change1)
# -------------------------------------------------------------------
"""
# """
# -----------------------------读取标定参数数据-----------------------------
first_occurance("Asap3ReadCalibrationObject")

calibrationObjectName = r"P_VMMSG01D20_AlgoSwitch"
format = TFormat.ECU_INTERNAL
c_format = ctypes.c_int(format)
read_object = 0 #TCalibrationObjectValue()
# read_object.value.value = ctypes.c_double(1)

c_calibrationObjectName = ctypes.c_char_p(calibrationObjectName.encode("UTF-8"))
c_read_object = ctypes.c_long(5)#ctypes.byref(read_object)
c_read_object_p = ctypes.byref(c_read_object)

dll.Asap3ReadCalibrationObject.restype = ctypes.c_bool
# dll.Asap3ReadCalibrationObject.argtypes = (
#     TAsap3Hdl,
#     ctypes.c_ushort,
#     ctypes.c_char_p,
#     ctypes.c_int,
#     ctypes.POINTER(TCalibrationObjectValue),
# )

result_read = dll.Asap3ReadCalibrationObject(
    handle,
    TModulHdl,
    c_calibrationObjectName,
    c_format,
    c_read_object_p,
)
print("cali read result:", result_read, '\n', c_read_object.value)
# print("标定数据读取结果：", result_read, '\n')
# ----------------------------------------------------------
# """
# """
# -----写入标定数据-----
first_occurance("Asap3WriteCalibrationObject")

# write_object = TCalibrationObjectValue()
# write_object.type = TValueType.VALUE
# write_object.value.value = ctypes.c_double(1)
write_object = 1
c_write_object = ctypes.c_long(1)
c_write_object_p = ctypes.byref(c_write_object)
c_read_object = ctypes.c_long(1)

dll.Asap3WriteCalibrationObject.restype = ctypes.c_bool
# dll.Asap3WriteCalibrationObject.argtypes = (
#     TAsap3Hdl,
#     ctypes.c_ushort,
#     ctypes.c_char_p,
#     ctypes.c_int,
#     ctypes.POINTER(TCalibrationObjectValue)
# )

result_write = dll.Asap3WriteCalibrationObject(
    handle,
    TModulHdl,
    c_calibrationObjectName,
    c_format,
    c_read_object_p,
)
print("标定数据写入结果:", result_write, '\n', c_read_object.value)
time.sleep(3)
result_read = dll.Asap3ReadCalibrationObject(
    handle,
    TModulHdl,
    c_calibrationObjectName,
    c_format,
    c_read_object_p,
)
print("标定数据读取结果：", result_read, '\n', c_read_object.value)
# """
# ---------------------查询对象信息------------------------
"""
xDimension = 0
yDimension = 0
c_x = ctypes.c_short(xDimension)
c_y = ctypes.c_short(yDimension)
c_x_p = ctypes.byref(c_x)
c_y_p = ctypes.byref(c_y)

dll.Asap3CalibrationObjectInfo.restype = ctypes.c_bool
dll.Asap3CalibrationObjectInfo.argtypes = [
    TAsap3Hdl,
    ctypes.c_ushort,
    ctypes.c_char_p,
    ctypes.POINTER(ctypes.c_short),
    ctypes.POINTER(ctypes.c_short),
]

result = dll.Asap3CalibrationObjectInfo(
    handle,
    TModulHdl,
    c_calibrationObjectName,
    c_x_p,
    c_y_p,
)
print(result)
--------------------------------------------------------------------
"""

# -----------------------------启动measurement-----------------------
# 获取当前ECU tasks
"""
first_occurance("Asap3GetEcuTasks")

maxTaskInfo = 10
taskInfo = TTaskInfo()
noTasks = 0


c_taskInfo_p = ctypes.byref(taskInfo)
c_noTasks = ctypes.c_ushort(noTasks)
c_noTasks_p = ctypes.byref(c_noTasks)
c_maxTaskInfo = ctypes.c_ushort(maxTaskInfo)

dll.Asap3GetEcuTasks.restype = ctypes.c_bool
dll.Asap3GetEcuTasks.argtypes = (
    TAsap3Hdl,
    ctypes.c_ushort,
    ctypes.POINTER(TTaskInfo),
    ctypes.POINTER(ctypes.c_ushort),
    ctypes.c_ushort,
)

get_task_result = dll.Asap3GetEcuTasks(
    handle,
    TModulHdl,
    c_taskInfo_p,
    c_noTasks_p,
    c_maxTaskInfo,
)

print("get_task_result: ",'\n',get_task_result,'\n', c_noTasks.value)
print(taskInfo.value)
print(taskInfo.taskId.value, taskInfo.taskCycle.value)

first_occurance("Asap3StartDataAcquisition")

dll.Asap3StartDataAcquisition.restype = ctypes.c_bool
dll.Asap3StartDataAcquisition.argtypes = (
    TAsap3Hdl,
)

start_measurement_result = dll.Asap3StartDataAcquisition(handle)

print("启动观测：", start_measurement_result)
"""
"""
# ----------------通过地址取值---------------------------
addr = 0x805F00DC #0x805F038C
addrExt = 0
size = 8
data = "d"
c_addr = ctypes.c_ulong(addr)
c_addrExt = ctypes.c_char(addrExt)
c_size = ctypes.c_ulong(size)
c_data = ctypes.c_char_p(data.encode("UTF-8"))

dll.Asap3ReadByAddress.restype = ctypes.c_bool
dll.Asap3ReadByAddress.argtypes = [
    TAsap3Hdl,
    ctypes.c_ushort,
    ctypes.c_ulong,
    ctypes.c_char,
    ctypes.c_ulong,
    ctypes.c_char_p
]

result = dll.Asap3ReadByAddress(
    handle,
    TModulHdl,
    c_addr,
    c_addrExt,
    c_size,
    c_data,
)

print(result, '\n', data)

# addr2 = 0x805F03E4 #0x805F038C
# data2 = "d"
# c_addr2 = ctypes.c_ulong(addr)
# c_data2 = ctypes.c_char_p(data2.encode("UTF-8"))
#
# result2 = dll.Asap3ReadByAddress(
#     handle,
#     TModulHdl,
#     c_addr2,
#     c_addrExt,
#     c_size,
#     c_data2,
# )

size2 = 8
c_size2 = ctypes.c_ulong(size2)
write_address = 0x805F00E0
c_write_address = ctypes.c_ulong(write_address)
write_data = b"\1"
c_write_data = ctypes.c_char_p(write_data)
result_write_address = dll.Asap3WriteByAddress(
    handle,
    TModulHdl,
    c_write_address,
    c_addrExt,
    c_size2,
    c_write_data,
)
time.sleep(20)
write_data2 = b"\7"
c_write_data2 = ctypes.c_char_p(write_data2)
result_write_address1 = dll.Asap3WriteByAddress(
    handle,
    TModulHdl,
    c_write_address,
    c_addrExt,
    c_size2,
    c_write_data,
)
print(result_write_address)
print("---")
time.sleep(20)
# -----------------------------------------------------------
"""
"""
# ------------------------终止measurement---------------------
first_occurance("Asap3StopDataAcquisition")

dll.Asap3StopDataAcquisition.restype = ctypes.c_bool
dll.Asap3StopDataAcquisition.argtypes = (
    TAsap3Hdl,
)
stop_measurenment_result = dll.Asap3StopDataAcquisition(handle)
print("停止观测：", stop_measurenment_result)
"""