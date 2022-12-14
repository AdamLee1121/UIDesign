
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testTool.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again. Do not edit this file unless you know what you are doing.
import time

from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from enum import Enum
from canoeClass import canoe, caseTxRxSig, test_log
from canapeClass import canape
# 设置显示框中字体大小，全局使用
font = QtGui.QFont()
font.setPointSize(12)
font.setBold(False)

# 设置日志等级
class loglevel(Enum):
    info = 0
    warning = 1
    error = 2

class Ui_Form(QtWidgets.QWidget):
    def __init__(self, Form):
        super(Ui_Form, self).__init__()
        self.setupUi(Form)
        self.case_num_list = []
        self.actual_out_list = []
        self.pass_fail_list = []

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(660, 550)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 631, 501))
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.textEdit_desc = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_desc.setGeometry(QtCore.QRect(280, 20, 351, 381))
        self.textEdit_desc.setObjectName("textEdit_desc")
        self.checkBox_kidding = QtWidgets.QCheckBox(self.tab_3)
        self.checkBox_kidding.setGeometry(QtCore.QRect(320, 410, 221, 16))
        self.checkBox_kidding.setObjectName("checkBox_kidding")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.tab_3)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 60, 261, 241))
        self.calendarWidget.setObjectName("calendarWidget")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 611, 371))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.CANoe_tab = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.CANoe_tab.setFont(font)
        self.CANoe_tab.setObjectName("CANoe_tab")
        self.verticalLayout.addWidget(self.CANoe_tab)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_oeconf = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_oeconf.setObjectName("lineEdit_oeconf")
        self.gridLayout.addWidget(self.lineEdit_oeconf, 1, 1, 1, 1)
        self.toolButton_oeconf = QtWidgets.QToolButton(self.verticalLayoutWidget)
        self.toolButton_oeconf.setObjectName("toolButton_oeconf")
        self.gridLayout.addWidget(self.toolButton_oeconf, 1, 2, 1, 1)
        self.label_cofg_file = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_cofg_file.setObjectName("label_cofg_file")
        self.gridLayout.addWidget(self.label_cofg_file, 1, 0, 1, 1)
        self.lineEdit_oedbc = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_oedbc.setObjectName("lineEdit_oedbc")
        self.gridLayout.addWidget(self.lineEdit_oedbc, 2, 1, 1, 1)
        self.label_dbc = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_dbc.setObjectName("label_dbc")
        self.gridLayout.addWidget(self.label_dbc, 2, 0, 1, 1)
        self.toolButton_oedbc = QtWidgets.QToolButton(self.verticalLayoutWidget)
        self.toolButton_oedbc.setObjectName("toolButton_oedbc")
        self.gridLayout.addWidget(self.toolButton_oedbc, 2, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.toolButton_apeconf = QtWidgets.QToolButton(self.verticalLayoutWidget)
        self.toolButton_apeconf.setObjectName("toolButton_apeconf")
        self.gridLayout_2.addWidget(self.toolButton_apeconf, 0, 2, 1, 1)
        self.label_cofg_file_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_cofg_file_2.setObjectName("label_cofg_file_2")
        self.gridLayout_2.addWidget(self.label_cofg_file_2, 0, 0, 1, 1)
        self.lineEdit_apeconf = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_apeconf.setObjectName("lineEdit_apeconf")
        self.gridLayout_2.addWidget(self.lineEdit_apeconf, 0, 1, 1, 1)
        self.label_device = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_device.setObjectName("label_device")
        self.gridLayout_2.addWidget(self.label_device, 1, 0, 1, 1)
        self.lineEdit_device = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_device.setObjectName("lineEdit_device")
        self.gridLayout_2.addWidget(self.lineEdit_device, 1, 1, 1, 1)
        self.label_a2l = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_a2l.setObjectName("label_a2l")
        self.gridLayout_2.addWidget(self.label_a2l, 2, 0, 1, 1)
        self.lineEdit_A2L = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_A2L.setObjectName("lineEdit_A2L")
        self.gridLayout_2.addWidget(self.lineEdit_A2L, 2, 1, 1, 1)
        self.toolButton_a2l = QtWidgets.QToolButton(self.verticalLayoutWidget)
        self.toolButton_a2l.setObjectName("toolButton_a2l")
        self.gridLayout_2.addWidget(self.toolButton_a2l, 2, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_single = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_single.setObjectName("pushButton_single")
        self.gridLayout_3.addWidget(self.pushButton_single, 2, 2, 1, 1)
        self.pushButton_all = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_all.setObjectName("pushButton_all")
        self.gridLayout_3.addWidget(self.pushButton_all, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 2, 0, 1, 1)
        self.label_case = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_case.setObjectName("label_case")
        self.gridLayout_3.addWidget(self.label_case, 0, 0, 1, 1)
        self.lineEdit_oecase = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_oecase.setObjectName("lineEdit_oecase")
        self.gridLayout_3.addWidget(self.lineEdit_oecase, 0, 1, 1, 1)
        self.toolButton_oecase = QtWidgets.QToolButton(self.verticalLayoutWidget)
        self.toolButton_oecase.setObjectName("toolButton_oecase")
        self.gridLayout_3.addWidget(self.toolButton_oecase, 0, 2, 1, 1)
        self.lineEdit_single = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_single.setText("")
        self.lineEdit_single.setObjectName("lineEdit_single")
        self.gridLayout_3.addWidget(self.lineEdit_single, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 3, 0, 1, 1)
        self.lineEdit_part = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_part.setObjectName("lineEdit_part")
        self.gridLayout_3.addWidget(self.lineEdit_part, 3, 1, 1, 1)
        self.pushButton_part = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_part.setObjectName("pushButton_part")
        self.gridLayout_3.addWidget(self.pushButton_part, 3, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.textBrowser_log = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_log.setGeometry(QtCore.QRect(50, 20, 501, 441))
        self.textBrowser_log.setObjectName("textBrowser_log")
        self.tabWidget.addTab(self.tab_2, "")

        # 选择信号槽
        self.checkBox_kidding.clicked.connect(self.joke_talk)
        self.toolButton_oedbc.clicked.connect(self.loadDBCCSV)
        self.toolButton_oeconf.clicked.connect(self.loadCfg_oe)
        self.toolButton_oecase.clicked.connect(self.loadCaseFiles)
        self.pushButton_all.clicked.connect(self.allTest)
        self.pushButton_single.clicked.connect(self.singleTest)
        self.pushButton_part.clicked.connect(self.partTest)
        self.toolButton_apeconf.clicked.connect(self.loadCfg_ape)
        self.toolButton_a2l.clicked.connect(self.loadA2l)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textEdit_desc.setHtml(_translate("Form",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">**********底盘电控标定测试组自动化测试工具**********</p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">------------------------------------------------------</p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">|适用范围：</p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">|  控制器开环测试</p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">|  输入值来源：CAN信号、标定量</p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">|  具备现成的 CANoe 和 CANape 工程文件</p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">------------------------------------------------------</p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">使用方法：</p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">CANoe配置：</p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1、选中配置文件，建议选择12.0版本</p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2、选择包含 即将使用的CAN信号 的dbc文件（理论上.csv也可以，但不建议），可多选</p>\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">CANape配置：</p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1、选中配置文件，建议选择18.0版本</p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2、节点填写配置文件中的XCP device名称，如 NOA_CAL，请勿添加引号，目前仅支持XCP节点</p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3、A2L名称填写与节点绑定的db文件名称，如 VMM_main_Updated.a2l，请勿添加引号</p>\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">测试用例：</p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">请按照规则编写测试用例，模板地址：</p>\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">执行用例：</p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1、全部执行：执行全部用例</p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2、单个用例：用例位置使用 sheet name,case order 表示，如 sheet1,88 （英文逗号&quot;,&quot;）</p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3、执行部分用例</p>\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">日志打印：</p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">非实时日志，测试结束后可见</p>\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.checkBox_kidding.setText(_translate("Form", "请阅读完成后勾选，再进入配置tab哦"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "说明"))
        self.CANoe_tab.setText(_translate("Form", "CANoe"))
        self.toolButton_oeconf.setText(_translate("Form", "..."))
        self.label_cofg_file.setText(_translate("Form", "配置文件"))
        self.label_dbc.setText(_translate("Form", "dbc文件"))
        self.toolButton_oedbc.setText(_translate("Form", "..."))
        self.label_3.setText(_translate("Form", "CANape"))
        self.toolButton_apeconf.setText(_translate("Form", "..."))
        self.label_cofg_file_2.setText(_translate("Form", "配置文件"))
        self.label_device.setText(_translate("Form", "节点名称"))
        self.label_a2l.setText(_translate("Form", "A2L名称"))
        self.toolButton_a2l.setText((_translate("Form", "...")))
        self.label_4.setText(_translate("Form", "Case & Execute"))
        self.pushButton_single.setText(_translate("Form", "执行"))
        self.pushButton_all.setText(_translate("Form", "执行全部用例"))
        self.label.setText(_translate("Form", "执行单个用例"))
        self.label_case.setText(_translate("Form", "测试用例"))
        self.toolButton_oecase.setText(_translate("Form", "..."))
        self.label_2.setText(_translate("Form", "执行部分用例"))
        self.pushButton_part.setText(_translate("Form", "执行"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "配置"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "日志"))

    def joke_talk(self):
        QtWidgets.QMessageBox.warning(self, '警告', '嘿嘿，你点它干嘛', QtWidgets.QMessageBox.Cancel)

    # 加载canoe配置
    def loadCfg_oe(self):
        dialog = QtWidgets.QFileDialog()
        url = dialog.getOpenFileName(self, "打开canoe配置文件", '.', '文件(*.cfg)')[0]
        self.lineEdit_oeconf.setText(url)

    def loadCfg_ape(self):
        dialog = QtWidgets.QFileDialog()
        url = dialog.getOpenFileName(self, "打开canoe配置文件", '.', '文件(*.cna)')[0]
        self.lineEdit_apeconf.setText(url)

    # 加载dbc文件（多个）
    def loadDBCCSV(self):
        dialog = QtWidgets.QFileDialog()
        url = dialog.getOpenFileNames(self, "打开文件", '.', '*.dbc; *.csv')[0]
        if type(url) == type(list()):
            url_out = ';'.join(url)
        else:
            url_out = url
        self.lineEdit_oedbc.setText(url_out)

    # 加载A2L
    def loadA2l(self):
        dialog = QtWidgets.QFileDialog()
        url = dialog.getOpenFileName(self, "打开文件", '.', 'A2L(*.a2l)')[0]
        self.lineEdit_A2L.setText(url)

    # 加载测试用例
    def loadCaseFiles(self):
        dialog = QtWidgets.QFileDialog()
        # 获取单个文件
        # url = dialog.getOpenFileName(self, "打开文件", '.', '表格 (*.xlsx)')[0]
        url = dialog.getOpenFileNames(self, "打开文件", '.', '表格 (*.xlsx)')[0]
        url_out = ''
        if type(url) == type(list()):
            url_out = ';'.join(url)
        else:
            url_out = url
        # print(url_out) # D:/liyi10/Desktop/ASU功能测试.xlsx;D:/liyi10/Desktop/testToolCase.xlsx
        # print(type(url_out)) # <class 'str'>
        self.lineEdit_oecase.setText(url_out)

    # 全部执行测试
    def allTest(self):
        if not self.lineEdit_oecase.text():
            QtWidgets.QMessageBox.warning(self, '警告', '请选择测试用例', QtWidgets.QMessageBox.Cancel)
        elif not self.lineEdit_oeconf.text():
            QtWidgets.QMessageBox.warning(self, '警告', '配置文件不能为空', QtWidgets.QMessageBox.Cancel)
        else:
            cfgPath_oe = self.lineEdit_oeconf.text()
            cfgPath_ape = self.lineEdit_apeconf.text()
            # ape工作文件夹
            workingDir = cfgPath_ape[:cfgPath_ape.rfind("/")]
            # ape device名称
            ape_device = self.lineEdit_device.text()
            # a2l名称
            ape_a2l = self.lineEdit_A2L.text().split("/")[-1]
        # cfgPath_oe = r"D:/liyi10/Downloads/CANoe/VMM/CANoe10-VMM.cfg"
        # cfgPath_ape = r"D:/liyi10/Downloads/X01_FSD_ACC_VMMSG_0627(1)/X01_FSD_ACC_VMMSG_0627/X01_FSD.cna"
        # workingDir = cfgPath_ape[:cfgPath_ape.rfind("/")]
        # dbcfilenames = r"D:/liyi10/project/VMM/X01-610VMM(1)/X01_CAN_Matrix_V6.0.0_20220510_FSD1_CHCAN1.dbc;D:/liyi10/project/VMM/X01-610VMM(1)/X01_CAN_Matrix_V6.0.0_20220510_FSD1_CHCAN2.dbc;D:/liyi10/project/VMM/X01-610VMM(1)/X01_CAN_Matrix_V6.0.0_20220510_FSD1_ICAN.dbc;D:/liyi10/project/VMM/X01-610VMM(1)/X01_CAN_Matrix_V6.0.1_20220511_FSD1_ECAN.dbc"
        # casefilename=r"D:/liyi10/Desktop/testToolDebug/testToolCase_ASU.xlsx"
        # ape_device = r"NOA_CAL"
        # ape_a2l = r"VMM_main_Updated.a2l"
            # 创建工具应用
            oe = canoe.CANoe()
            ape = canape.CANape()
            self.log_display("info", "starting test...")
            # 打开工程
            oe.cfg_open(cfgPath_oe)
            ape.initial(workingDir=workingDir, device_name=ape_device, db_name=ape_a2l)
            # 启动观测
            oe.start_Measurement()
            mdfname = "Autotest" + time.strftime('%Y-%m-%d-%H-%M-%S')
            ape.application.Measurement.MDFFilename = mdfname
            ape.measurement_start() # 数据记录文件名
            print("start measuring.", mdfname)

            # caseTxRxSig.CaseTxRxSig.verify(self, oe=oe, ape= ape, casefilename=casefilename,dbcfilenames=dbcfilenames.split(";"))

            self.case_num_list, self.actual_out_list, self.pass_fail_list = \
                caseTxRxSig.CaseTxRxSig.verify(self, oe=oe, ape=ape, casefilename=self.lineEdit_oecase.text(),
                                               dbcfilenames=self.lineEdit_oedbc.text().split(";"))
            # 结束观测
            oe.stop_Measurement()
            ape.measurement_stop()
            # reporter(self.case_num_list, self.actual_out_list, self.pass_fail_list)
            print('allTest done!')

    # 执行单个测试
    def singleTest(self):
        cfgPath_oe = self.lineEdit_oeconf.text()
        cfgPath_ape = self.lineEdit_apeconf.text()
        # ape工作文件夹
        workingDir = cfgPath_ape[:cfgPath_ape.rfind("/")]
        # ape device名称
        ape_device = self.lineEdit_device.text()
        # a2l名称
        ape_a2l = self.lineEdit_A2L.text()
        # 用例位置信息
        case_info = self.lineEdit_single.text()
        # 创建工具应用
        oe = canoe.CANoe()
        ape = canape.CANape()
        self.log_display("info", "starting test...")
        # 打开工程
        # oe.cfg_open(cfgPath_oe)
        # ape.initial(workingDir = workingDir)
        # 启动观测
        # oe.start_Measurement()
        # mdfname = ape.measurement_start() # 数据记录文件名
        print("start measuring.")
        self.actual_out_list, self.pass_fail_list = \
            caseTxRxSig.CaseTxRxSig.verify_single(self, oe=oe, ape=ape, casefilename=self.lineEdit_oecase.text(),
                                                  dbcfilenames=self.lineEdit_oedbc.text().split(";"),
                                                  sheetname=case_info[0], caseorder=case_info[1],
                                                  device_name=ape_device, db_name=ape_a2l)
        # 结束观测
        # oe.stop_Measurement()
        # ape.measurement_stop()
        # reporter(self.case_num_list, self.actual_out_list, self.pass_fail_list)
        print('singleTest done!')

    def partTest(self):
        text = self.lineEdit_part.text()
        text = text.split(";")

    # 日志展示
    def log_display(self, level: str, text: str):
        # 设置日志窗口字体大小
        self.textBrowser_log.setFont(font)
        pathsplit = self.lineEdit_oecase.text().split('/')
        filesplit = pathsplit[-1].split('.')
        casefile_name = filesplit[0]
        logger = test_log.Log("标定测试部-" + casefile_name).get_log()
        if level == "info":
            logger.info(text)
            self.textBrowser_log.append(text)

        if level == "warning":
            logger.warning(text)
            self.textBrowser_log.append(text)

        if level == "error":
            logger.error(text)
            self.textBrowser_log.append("<font color='red'>" + text + "<font>")

    # def report(self):
    #     Reporter.report(self.case_num_list, self.actual_out_list, self.pass_fail_list)

# import sys
# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     w = QtWidgets.QWidget()
#     ui = Ui_Form(w)
#     ui.allTest()


