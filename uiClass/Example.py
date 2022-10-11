# 创建简单对话框

# from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QInputDialog
#
#
# class Example(QWidget):
#
#     def __init__(self):
#         super(Example, self).__init__()
#         self.btn = None
#         self.le = None
#         self.initUI()
#
#     def initUI(self):
#         self.btn = QPushButton("Dialog", self)
#         self.btn.move(20, 20)
#         self.btn.clicked.connect(self.showDialog())
#         self.le = QLineEdit(self)
#         self.le.move(130, 20)
#
#         self.setWindowTitle("Input Dialog")
#         self.show()
#
#     def showDialog(self):
#         text, ok = QInputDialog.getText(self, "Input Dialog", "Enter your name.")
#         if ok:
#             self.le.setText(str(text))

from PyQt5