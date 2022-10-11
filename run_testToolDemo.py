import sys
from uiClass import ui_form
from PyQt5.QtWidgets import QApplication, QWidget

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    ui = ui_form.Ui_Form(w)
    # ui.setupUi(w)
    w.setWindowTitle('通讯测试自动化工具')
    w.show()
    sys.exit(app.exec_())