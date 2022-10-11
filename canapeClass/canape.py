# -*-coding: "utf-8"-*-

"""
# File:        canape.py
# Author:      "liyi"
# CreateTime:  2022/8/10 10:15
# Version:     python 3.6
# Description: 封装CANape的API。包括初始化 canape_init5，加载已有工程文件 load_config
               获取device数量 canape_device_count，XCP数据获取 canape_cali_read,
               XCP数据写入 canape_cali_write,启动观测 canape_measurement_start，
               停止观测 canape_measurement_stop，退出CANape canape_exit
"""
import time
import ctypes
from enum import IntEnum
from os import getcwd
from win32com.client import *
from win32com.client.connect import *
from uiClass import ui_form
"""
# -------------------------继承dll中的数据结构---------------------------------
class struct_tAsap3Hdl(ctypes.Structure):
    pass


class ushort_tModulHdl(ctypes.c_ushort):
    pass


class value(ctypes.Structure):
    pass
value._fields_ = [
    ("type", ctypes.c_int),
    ("value", ctypes.c_double)
]


class axis(ctypes.Structure):
    pass
axis._fields_ = [
    ("type", ctypes.c_int),
    ("dimension", ctypes.c_short),
    ("axis", ctypes.POINTER(ctypes.c_double))
]


class ascii(ctypes.Structure):
    pass
ascii._fields_ = [
    ("type", ctypes.c_int),
    ("len", ctypes.c_short),
    ("ascii", ctypes.c_char_p)
]


class curve(ctypes.Structure):
    pass
curve._fields_ = [
    ("type", ctypes.c_int),
    ("dimension", ctypes.c_short),
    ("axis", ctypes.POINTER(ctypes.c_double)),
    ("values", ctypes.POINTER(ctypes.c_double))
]


class map(ctypes.Structure):
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
    pass
valblk._fields_ = [
    ("type", ctypes.c_int),
    ("xDimension", ctypes.c_short),
    ("yDimension", ctypes.c_short),
    ("values", ctypes.POINTER(ctypes.c_double))
]


class TCalibrationObjectValue(ctypes.Union):
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


class Mode(IntEnum):
    e_TR_MODE_RAM = 0
    e_TR_MODE_ROM = 1

class CANape():
    def __init__(self, cfg_path: str):
        self.m_cfgpath = cfg_path
        header_file = getcwd()+r"\canapeClass\CANapAPI.h"
        CANapAPI_dll = getcwd()+r"\canapeClass\CANapAPI64.dll"
        self.dll = ctypes.windll.LoadLibrary(CANapAPI_dll)
        self.TAsap3Hdl = ctypes.POINTER(struct_tAsap3Hdl)
        self._handle = self.TAsap3Hdl()
        self._handle_p = ctypes.byref(self._handle)

        self.TModulHdl = ctypes.c_ushort()
        self.handle_p_m = ctypes.byref(self.TModulHdl)

    def canape_init5(self):
        index_cut = self.m_cfgpath.rfind(r'/', 0, len(self.m_cfgpath))
        _workingDir = self.m_cfgpath[:index_cut]
        responseTimeout = 10000
        fifoSize = 8192
        sampleSize = 256
        debugMode = True
        clearDeviceList = False
        bHexmode = False
        bModalMode = True

        c_responseTimeout = ctypes.c_ulong(responseTimeout)
        c_workingDir = ctypes.c_char_p(_workingDir.encode("UTF-8"))
        c_fifoSize = ctypes.c_ulong(fifoSize)
        c_sampleSize = ctypes.c_ulong(sampleSize)
        c_debugMode = ctypes.c_bool(debugMode)
        c_clearDeviceList = ctypes.c_bool(clearDeviceList)
        c_bHexmode = ctypes.c_bool(bHexmode)
        c_bModalMode = ctypes.c_bool(bModalMode)

        self.dll.Asap3Init5.restype = ctypes.c_bool
        self.dll.Asap3Init5.argtypes = (
            ctypes.POINTER(self.TAsap3Hdl),
            ctypes.c_ulong,
            ctypes.c_char_p,
            ctypes.c_ulong,
            ctypes.c_ulong,
            ctypes.c_bool,
            ctypes.c_bool,
            ctypes.c_bool,
            ctypes.c_bool
        )

        ape = self.dll.Asap3Init5(
            self._handle_p,
            c_responseTimeout,
            c_workingDir,
            c_fifoSize,
            c_sampleSize,
            c_debugMode,
            c_clearDeviceList,
            c_bHexmode,
            c_bModalMode,
        )

    def load_config(self):
        configFileName = self.m_cfgpath.split("/")[-1]
        if not configFileName.endswith("cna"):
            raise Exception("Not correct canape project file!")
        c_configFileName = ctypes.c_char_p(configFileName.encode("UTF-8"))

        self.dll.Asap3LoadCNAFile.restype = ctypes.c_bool
        self.dll.Asap3LoadCNAFile.argtypes = (
            self.TAsap3Hdl,
            ctypes.c_char_p,
        )

        self.dll.Asap3LoadCNAFile(
            self._handle,
            c_configFileName,
        )

    def get_version(self):
        appversion = Appversion()
        c_appversion = ctypes.byref(appversion)
        self.dll.Asap3GetApplicationVersion.restype = ctypes.c_bool
        self.dll.Asap3GetApplicationVersion.argtypes = [
            self.TAsap3Hdl,
            ctypes.POINTER(Appversion),
        ]
        self.dll.Asap3GetApplicationVersion(
            self._handle,
            c_appversion,
        )
        return appversion.MainVersion

    def device_count(self):
        count = 10
        c_count = ctypes.c_ulong(count)
        c_count_p = ctypes.byref(c_count)
        self.dll.Asap3GetModuleCount.restype = ctypes.c_bool
        self.dll.Asap3GetModuleCount.argtypes = (
            self.TAsap3Hdl,
            ctypes.POINTER(ctypes.c_ulong),
        )
        self.dll.Asap3GetModuleCount(
            self._handle,
            c_count_p,
        )
        return c_count.value # 设备数量

    def device_active(self):
        device_act = False
        c_device_act = ctypes.c_bool(device_act)
        c_device_act_p = ctypes.byref(c_device_act)
        self.dll.Asap3IsModuleActive.restype = ctypes.c_bool
        self.dll.Asap3IsModuleActive.argtypes = (
           self.TAsap3Hdl,
            ctypes.c_ushort,
            ctypes.POINTER(ctypes.c_bool)
        )

        self.dll.Asap3IsModuleActive(
            self._handle,
            self.TModulHdl,
            c_device_act_p,
        )

    def switch_cali_mode(self, mode: int):
        cali_mode = -1
        if mode == 0:
            cali_mode = Mode.e_TR_MODE_ROM
        if mode == 1:
            cali_mode = Mode.e_TR_MODE_RAM
        c_cali_mode = ctypes.c_int(cali_mode)

        switch_result = self.dll.Asap3SwitchToMemoryPage(
            self._handle,
            self.TModulHdl,
            c_cali_mode
        )
        return switch_result

    def read_caliobject_by_name(self, caliobject_name: str):
        calibrationObjectName = caliobject_name
        format = TFormat.PHYSICAL_REPRESENTATION
        c_format = ctypes.c_int(format)

        read_object = TCalibrationObjectValue()
        read_object.value.value = ctypes.c_double()

        c_calibrationObjectName = ctypes.c_char_p(calibrationObjectName.encode("UTF-8"))
        c_read_object_p = ctypes.byref(read_object)

        self.dll.Asap3ReadCalibrationObject.restype = ctypes.c_bool
        self.dll.Asap3ReadCalibrationObject.argtypes = (
            self.TAsap3Hdl,
            ctypes.c_ushort,
            ctypes.c_char_p,
            ctypes.c_int,
            ctypes.POINTER(TCalibrationObjectValue),
        )

        result_read = self.dll.Asap3ReadCalibrationObject(
            self._handle,
            self.TModulHdl,
            c_calibrationObjectName,
            c_format,
            c_read_object_p,
        )

        return read_object.value.value

    def write_caliobject_by_name(self, caliobject_name: str, set_value):
        calibrationObjectName = caliobject_name
        format = TFormat.PHYSICAL_REPRESENTATION
        c_format = ctypes.c_int(format)
        write_object = TCalibrationObjectValue()
        write_object.type = TValueType.VALUE
        write_object.value.value = ctypes.c_double(set_value)

        c_calibrationObjectName = ctypes.c_char_p(calibrationObjectName.encode("UTF-8"))
        c_write_object_p = ctypes.byref(write_object)

        self.dll.Asap3WriteCalibrationObject.restype = ctypes.c_bool
        self.dll.Asap3WriteCalibrationObject.argtypes = (
            self.TAsap3Hdl,
            ctypes.c_ushort,
            ctypes.c_char_p,
            ctypes.c_int,
            ctypes.POINTER(TCalibrationObjectValue)
        )

        result_write = self.dll.Asap3WriteCalibrationObject(
            self._handle,
            self.TModulHdl,
            c_calibrationObjectName,
            c_format,
            c_write_object_p,
        )

    def read_caliobject_by_address(self, address, ):
        addr = int(address, 16)
"""

class CANape():
    def __init__(self):
        self.application = Dispatch('CANape.Application')
        print('CANape dispatched.')
        self.device = None
        # ui_form.Ui_Form.log_display("info", 'CANape dispatched.')
        # self.ver = self.application.APPVersion
        # print(f"CANape {self.ver.Main} has been loaded...")
        # ui_form.Ui_Form.log_display("info", f"CANape {self.ver} has been loaded...")

    def initial(self, workingDir: str, device_name:str, db_name: str):
        self.application.Open1(workingDir, 0, 50000, True) # 工作文件夹， 是否显示窗口， 超时时间， 是否为non-modal mode
        print("CANape initialized.")
        # ui_form.Ui_Form.log_display("info", "CANape initialized.")
        self.device = self.application.Devices.Add(device_name, db_name, "XCP", 1)
        print("device added.")


    def read_by_name(self, object_name: str):
        try:
            calob = self.device.CalibrationObjects.Item(object_name)
        except:
            self.device.CalibrationObjects.Add(object_name)
            calob = self.device.CalibrationObjects.Item(object_name)

        Val = calob.Value
        return calob, Val


    def calibration_by_name(self, object_name: str, set_val):
        calob, _ = self.read_by_name(object_name)

        calob.Value = set_val
        calob.Write()

        # time.sleep(1)
        # calob.Read()
        # Val = calob.Value
        #
        # if Val == set_val:
        #     pass
        # else:
        #     print(f"参数 {object_name} 标定失败")


    def measurement_start(self):
        mea = self.application.Measurement.Start()
        time.sleep(5)
        if self.application.Measurement.Running:
            print("ape measurement is running!")
        else:
            print("Measurement is not started")
        # return mdfname


    def measurement_stop(self):
        if self.application.Measurement.Running:
            print(self.application.Measurement.MDFFilename)
            self.application.Measurement.Stop()
            print("end")
        else:
            pass


    def quit(self):
        self.application.Quit()

# ape = CANape()
# workingDir = "D:/liyi10/Downloads/X01_FSD_ACC_VMMSG_0627(1)/X01_FSD_ACC_VMMSG_0627"
# device_name = "NOA_CAL"
# db_name = "VMM_main_Updated.a2l"
# ape.initial(workingDir, device_name, db_name)
# ape.application.Measurement.MDFFilename="111.mdf"
# ape.measurement_start()
# va = ape.read_by_name("In_ESP_WheelBrkForceFL")
# print("In_ESP_WheelBrkForceFL:", va)
# print(ape.application.Measurement.MDFFilename)
# # ape.calibration_by_name("P_VMMSG_ADSAELevel", 0)
# # time.sleep(3)
# # ape.calibration_by_name("P_VMMSG_ADSAELevel", 1)
# # time.sleep(3)
# # ape.calibration_by_name("P_VMMSG_ADSAELevel", 2)
# time.sleep(5)
# ape.measurement_stop()
# ape.quit()