from canoeClass import canoe
from canapeClass import canape
import time

oe = canoe.CANoe()
oe.cfg_open(r"D:/liyi10/Downloads/CANoe/VMM/CANoe10-VMM.cfg")

ape = canape.CANape()
ape.initial(r"D:\liyi10\Downloads\X01_FSD_ACC_VMMSG_0627(1)\X01_FSD_ACC_VMMSG_0627",1,50000,True)
print('ape initialized.')

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

