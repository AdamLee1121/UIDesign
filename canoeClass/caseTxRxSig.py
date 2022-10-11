# -*- coding: utf-8 -*-

# 从测试用例Excel中获取 Tx signal 和 Rx signal
# 对 Tx 进行赋值并发送到总线上
# 获取 Rx 供后续断言使用
#
# Created by: liyi10@lixiang.com
#
# WARNING: Any manual changes made to this file will cause error!

import datetime
import threading
import pythoncom

from canoeClass.canoe import CANoe
import time
from copy import deepcopy
from canoeClass.data_process import DataProcess, csvload, DBCload
from uiClass import ui_form
from canapeClass.canape import CANape
from multiprocessing import Pool
from multiprocessing.dummy import Pool

# 提取到的输入步骤中，消息、信号、输入值的位置
location_msg = 0
location_sig = 1
location_set_val = 2
location_dbc_name = 3
location_cycle_time = 4
location_expect = 2

# location_delay = 3 # 预留等待时间的位置
# 从输入信号矩阵中提取出需要设置的Tx信号的，通道编号、消息名称、信号名称
class CaseTxRxSig():
    def __init__(self):
        pass

    def verify(self, oe: CANoe, ape:CANape,  casefilename: str,
               dbcfilenames, csvfilename: str=None):
        """
        两种场景：
        1、只输入一个测试用例文档，提取出其中的输入和预期输出。执行前置条件和操作步骤，对比输出
        2、输入多个测试用例文档，提取出其中的输入和预期输出，并整合。执行前置条件和操作步骤，对比暑促
        :param oe: CANoe应用
        :param filename: 
        :param filenames: 
        :return: None
        """
        global myThread
        time0 = time.time()

        case_num_list = []
        actual_out_list = []  # 所有用例的实际输出
        pass_fail_list = []
        if casefilename:
            case_data = DataProcess(filepath=casefilename)
            _, case_num_list = case_data.loadExcel()
            case_num_list = case_num_list.values()
            # ui_form.Ui_Form.log_display(self, "info", "case data has been loaded!")
            print("case_data has been loaded!")

            # app.start_Measurement()
            # 输入文档为DBC
            if dbcfilenames:
                parsedbc = {}
                for dbcfilename in dbcfilenames:
                    dbc = DBCload(dbcfilename)
                    dict_dbc = dbc.parseDBC()
                    parsedbc = dict(**parsedbc, **dict_dbc)

                print("dbcfiles has been loaded!")


                input, output = case_data.extract_sig_val(parseDBC=parsedbc)
                # print("output", output)
                print("正在执行...")
                case_num = len(input)

                i = 0
                while i < case_num:
                    inport_op = input[i]
                    if inport_op:
                        for n in range(len(inport_op)):
                            print(inport_op[n])

                        #     # if time_delay:
                        #     #     time.sleep(time_delay)  预留输入步骤之间的时间间隔
                        #     # myThread = threading.Thread(target=send_signal, args=(oe, ape, item_input))
                        #     # myThread.start()
                        #         cycle_time = self.send_signal(oe, ape, item_input)
                        #         oe.DoEvents(cycle_time)
                        # ----------------------BELOW AVAILABLE
                            count = 0
                            while count<100:
                                if len(inport_op[n]) == 5:
                                    count+=1
                                else:
                                    count = 100
                                send_signal(oe, ape, inport_op[n])

                    # time.sleep(1)
                    actual_out_per_case = [] #  每个用例的测试结果
                    if_pass_flag = True
                    for item_output in output[i]:
                        '''
                        msg_name_out = item_output[location_msg]
                        sig_name_out = item_output[location_sig]
                        expect_out = float(item_output[location_expect])
                        actual_out = app.get_sigVal(channel_num, msg_name_out, sig_name_out)
                        # print(expect_out, actual_out)
                        actual_out_per_case.append(sig_name_out + "=" + str(actual_out))
                        ui_form.Ui_Form.log_display(self, "info",
                                                    f"{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} "
                                                    f"-> 用例{i},信号{msg_name_out} {sig_name_out} 的预期输出："
                                                    f"{expect_out},实际输出：{actual_out}")
                        '''
                        expect_out, actual_out = get_signal(oe, ape, item_output, i+1)
                        # 收集每个输出信号的实际结果
                        actual_out_per_case.append(actual_out)
                        try:
                            assert float(expect_out) == float(actual_out), "Actual output doesn't equal to expect!"
                        except AssertionError as e:
                            if_pass_flag = False
                            ui_form.Ui_Form.log_display(self, "error", f"******{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
                                                                       f"-> 用例{i+1} "
                                                                       f"Actual output doesn't equal to expect!")
                    actual_out_list.append(deepcopy(actual_out_per_case))
                    if if_pass_flag:
                        pass_fail_list.append("PASS")
                    else:
                        pass_fail_list.append("Fail")
                    i += 1
                    time.sleep(5)
                    if inport_op:
                        for n in range(len(inport_op)):
                            if len(inport_op[n])==5:
                                inport_op[n][location_set_val]=0
                            else:
                                inport_op[n][1]=0
                            send_signal(oe, ape, inport_op[n])
                print(case_num_list, actual_out_list, pass_fail_list)

            else:
                ui_form.Ui_Form.log_display(self, "error", "DBC files are not found")

            if csvfilename:
                channel_num = 1
                cycle_time = 10
                csv = csvload(csvfilename)
                parsecsv = csv.parse_csv()
                print("extracting.")

                input, output = case_data.extract_sig_val(parseCSV=parsecsv)
                print("verify 正在执行...")
                case_num = len(input)
                # 每个信号的周期发送次数，后续会根据信号发送周期分类进行改进。1、仅触发三次的信号；2、持续信号，无等待时间；
                # 3、持续信号，有等待时间，发送次数=等待时间/发送周期
                cycle_count = 5  # 触发次数
                for i in range(case_num):
                    for count in range(cycle_count):
                        for item_input_step in input[i]:
                            msg_name_in = item_input_step[location_msg]
                            sig_name_in = item_input_step[location_sig]
                            set_val_in = item_input_step[location_set_val]
                            oe.set_sigVal(channel_num, msg_name_in, sig_name_in, set_val_in)
                            print("发送信号：", channel_num, msg_name_in, sig_name_in, set_val_in)
                            # time.sleep(delay) 预留各操作之间的等待时间
                            print("yes")
                        time.sleep(cycle_time / 1000)

                    time.sleep(1)

                    for item_output in output[i]:
                        msg_name_out = item_output[location_msg]
                        sig_name_out = item_output[location_sig]
                        expect_out = float(item_output[location_expect])
                        actual_out = oe.get_sigVal(channel_num, msg_name_out, sig_name_out)
                        print(expect_out, actual_out)
                        ui_form.Ui_Form.log_display(self, "info",
                                                    f"{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} "
                                                    f"-> 用例{i},信号{msg_name_out} {sig_name_out} 的预期输出："
                                                    f"{expect_out},实际输出：{actual_out}")
                        try:
                            assert expect_out == actual_out, "Actual output doesn't equal to expect!"
                        except AssertionError as e:
                            ui_form.Ui_Form.log_display(self, "error", "****** Actual output doesn't equal to expect!")

        else:
            ui_form.Ui_Form.log_display(self, "error", "case file not been loaded!")

        time1 = time.time()
        period = time1 - time0
        print("全部运行循环总耗时" + str(period))

        return case_num_list, actual_out_list, pass_fail_list

    def verify_single(self, oe: CANoe, ape: CANape, casefilename: str,
                      dbcfilenames: list=None, csvfilename: str="",
                      sheetname: str="Sheet2", caseorder: str="3",):
        """
        通过输入的”sheet名称, 用例序号“，查找用例内容，并执行测试步骤
        :param caseorder:
        :param oe: 连接的CANoe应用
        :param casefilename:测试用例文件路径
        :param sheetname: 单例所在的sheet名
        :param dbcfilenames:dbc文件列表
        :param csvfilename:
        :return:
        """
        case_order = int(caseorder)
        time0 = time.time()

        actual_out_list = []  # 所有用例的实际输出
        pass_fail_list = []
        if casefilename:
            case_data = DataProcess(casefilename)
            print("single case data done.")

            if dbcfilenames:
                parsedbc = {}
                for dbcfilename in dbcfilenames:
                    dbc = DBCload(dbcfilename)
                    parsedbc.update(dbc.parseDBC())

                input, output = case_data.extract_sig_val_single(parseDBC=parsedbc, sheet_name=sheetname, case_order=case_order)
                print("正在执行...")

                for item_input in input:
                    # if time_delay:
                    #     time.sleep(time_delay)  预留输入步骤之间的时间间隔
                    myThread = threading.Thread(target=self.send_signal, args=(oe, ape, item_input))
                    myThread.start()

                time.sleep(10)
                actual_out_per_case = []  # 每个用例的测试结果
                if_pass_flag = True
                for item_output in output:
                    '''
                    msg_name_out = item_output[location_msg]
                    sig_name_out = item_output[location_sig]
                    expect_out = float(item_output[location_expect])
                    actual_out = app.get_sigVal(channel_num, msg_name_out, sig_name_out)
                    # print(expect_out, actual_out)
                    actual_out_per_case.append(sig_name_out + "=" + str(actual_out))
                    ui_form.Ui_Form.log_display(self, "info",
                                                f"{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} "
                                                f"-> 用例{i},信号{msg_name_out} {sig_name_out} 的预期输出："
                                                f"{expect_out},实际输出：{actual_out}")
                    '''
                    expect_out, actual_out = self.get_signal(oe, item_output, case_order)
                    try:
                        assert expect_out == actual_out, "Actual output doesn't equal to expect!"
                    except AssertionError as e:
                        if_pass_flag = False
                        ui_form.Ui_Form.log_display(self, "error", "****** Actual output doesn't equal to expect!")
                actual_out_list.append(actual_out_per_case)
                if if_pass_flag:
                    pass_fail_list.append("PASS")
                else:
                    pass_fail_list.append("Fail")
                time.sleep(10)

            '''
            # 如果加载的CAN描述文件为CSV
            if csvfilename:
                csv = csvload(csv_name_in=csvfilename)
                print("extracting...")

                input, output = case_data.extract_sig_val_single(parseCSV=csv, sheet_name=sheetname, case_order=case_order)

                cycle_count = 5
                for count in range(cycle_count):
                    for item_input_step in input:
                        msg_name_in = item_input_step[location_msg]
                        sig_name_in = item_input_step[location_sig]
                        set_val_in = item_input_step[location_set_val]
                        app.set_sigVal(channel_num, msg_name_in, sig_name_in, set_val_in)
                        print("发送信号：", channel_num, msg_name_in, sig_name_in, set_val_in)
                        # time.sleep(delay) 预留各操作之间的等待时间
                        print("yes")
                    time.sleep(cycle_time / 1000)

                time.sleep(1)

                for item_output in output:
                    msg_name_out = item_output[location_msg]
                    sig_name_out = item_output[location_sig]
                    expect_out = float(item_output[location_expect])
                    actual_out = app.get_sigVal(channel_num, msg_name_out, sig_name_out)
                    print(expect_out, actual_out)
                    ui_form.Ui_Form.log_display(self, "info", f"{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} "
                                                              f"-> 用例{case_order},信号{msg_name_out} {sig_name_out} 的预期输出："
                                                              f"{expect_out},实际输出：{actual_out}")
                    try:
                        assert expect_out == actual_out, "Actual output doesn't equal to expect!"
                    except AssertionError as e:
                        ui_form.Ui_Form.log_display(self, "error", "****** Actual output doesn't equal to expect!")
                '''
        time1 = time.time()
        period = time1 - time0
        print("循环总耗时" + str(period))

        return actual_out_list, pass_fail_list

    def verify_range(self, oe:CANoe, ape: CANape, casefilename: str, dbcfilename: list=None,
                     csvfilename: str="", case_location: str="Sheet2,[1:3]; Sheet3,[1:3]"):
        case_location_list = case_location.split(";")
        for item_case_location in case_location_list:
            case_sheet_name = item_case_location.split(",")[0]
            case_range = item_case_location.split(",")[1]
            case_range_start = list(case_range)[1]
            case_range_end = list(case_range)[3]

            out_dict = {}

            actual_out_list = []
            pass_fail_list = []
            i = case_range_start
            while i <= case_range_end:
                actual_out, pass_fail = \
                    self.verify_single(oe, ape, casefilename, dbcfilename, sheetname=case_sheet_name, caseorder=i)
                actual_out_list.append(actual_out)
                pass_fail_list.append(pass_fail)
                i+=1

            out_dict.update({case_sheet_name: [case_range_start, case_range_end, actual_out_list, pass_fail_list]})

        return out_dict

def channel_choose(dbc_name) -> int:
    """
    根据dbc文件的名字选择对应的CAN通道
    通道设置：
    CHCAN1    1
    CHCAN2    2
    ICAN      3
    ECAN      4
    :param dbc_name:  DBC文件名称，来自于数据处理
    :return: int 通道号
    """
    if dbc_name == "CHCAN1":
        channel_num = 1
    elif dbc_name == "CHCAN2":
        channel_num = 2
    elif dbc_name == "ICAN":
        channel_num = 3
    else:
        channel_num = 4
    return channel_num

def send_signal(oe, ape, case_input: list):
    """
    利用CANoe发送CAN信号，CANape标定变量
    :param oe: CANoe Instance
    :param ape: CANape Instance
    :param case_input: case 输入序列
    :return:
    """
    # 为标定量初始化线程间隔时间
    cycle_time_thread = 100
    if len(case_input)==5:
        msg_name_in = case_input[location_msg]
        sig_name_in = case_input[location_sig]
        set_val_in = case_input[location_set_val]
        dbc_name = case_input[location_dbc_name]
        cycle_time_thread = float(case_input[location_cycle_time])/1000.0
        channel_num = channel_choose(dbc_name)
        oe.set_sigVal(channel_num=channel_num, msg_name=msg_name_in, sig_name=sig_name_in, setVal=set_val_in)
        # oe.DoEvents(cycle_time_thread)

    if len(case_input)==2 and case_input[0].startswith("env_"):
        oe.set_Envar(case_input[0], float(case_input[1]))

    if len(case_input)==2 and case_input[0].startswith("P_"):
        ape.calibration_by_name(case_input[0], int(case_input[1]))
        # ape.calibration_by_name("P_VMMSG_ADSAELevel", 1)

    # timer_0 = threading.Timer(interval=cycle_time_thread, function=send_signal,
    #                           args=(oe, ape, case_input))
    # timer_0.start()

def get_signal(oe, ape, case_expect: list, case_order:int):
    if len(case_expect) == 4:
        msg_name_out = case_expect[location_msg]
        sig_name_out = case_expect[location_sig]
        expect_out = case_expect[location_expect]
        dbc_name = case_expect[location_dbc_name]
        channel_num = channel_choose(dbc_name)
        actual_out = oe.get_sigVal(channel_num=channel_num, msg_name=msg_name_out,
                                   sig_name=sig_name_out)
        print(
            f"{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} "f"-> 用例{case_order},信号{msg_name_out} {sig_name_out} 的预期输出：",
            f"{expect_out},实际输出：{actual_out}")

        # ui_form.Ui_Form.log_display("info",
        #                             f"{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} "
        #                             f"-> 用例{case_order},信号{msg_name_out} {sig_name_out} 的预期输出："
        #                             f"{expect_out},实际输出：{actual_out}")

    else:
        # 获取标定量名称
        obj_name = case_expect[0]
        expect_out = case_expect[1]

        _, actual_out = ape.read_by_name(obj_name)
        print(
            f"{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')} "f"-> 用例{case_order},信号{obj_name} 的预期输出：",
            f"{expect_out},实际输出：{actual_out}")


    return expect_out, actual_out

# if __name__ == "__main__":
#     app = CANoe()
#     # app.cfg_open(r'D:/liyi10/Downloads/ASC110_TEST_220617/ASC110_TEST_1109.cfg')
#     app.start_Measurement()
#     casefilename = r'D:/liyi10/Desktop/testToolCase.xlsx'
#     test = CaseTxRxSig()
#     test.verify(app=app, casefilename=casefilename)
