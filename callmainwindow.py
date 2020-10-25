import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMessageBox
from mainwindow import *
from mainwindowsignal1 import *
from snmp import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
# 主窗口
class Mymainwindow(QMainWindow, Ui_MainWindow):
    # 默认的CPU阈值为100
    cpumax = '100'
    cpunow = '0'
    def __init__(self, parent=None):
        super(Mymainwindow, self).__init__(parent)
        #self.setWindowTitle("主界面")
        self.setupUi(self)
        self.timer = QTimer(self)  # 初始化一个定时器
        self.timer.timeout.connect(self.operate)  # 计时结束调用operate()方法
        self.timer.start(2000)  # 设置计时间隔并启动
        self.pushButton.clicked.connect(self.pushButton_func)
        self.pushButton_2.clicked.connect(self.pushButton_2_func)
        self.pushButton_3.clicked.connect(self.pushButton_3_func)
        self.pushButton_4.clicked.connect(self.pushButton_4_func)
        self.pushButton_5.clicked.connect(self.pushButton_5_func)
        self.pushButton_6.clicked.connect(self.pushButton_6_func)
        #self.Mywidget
        # 连接信号
        #mywidget.Signal.connect(self.getData)

    def pushButton_func(self):
        # 连接信号
        #mywin1 = Mymainwindow()
        mywidget.signal.connect(self.getData)
        #self.lineEdit.setText('str1')
        mywidget.show()
        #mywin._signal.connect(self.getData)

    # 接收信号后处理函数
    def getData(self, str1):
        self.lineEdit.setText(str1)

    def pushButton_2_func(self):
        data_2 = getCPU(self.lineEdit.text())
        self.lineEdit_2.setText(data_2)

    def pushButton_3_func(self):
        data_3 = getDisk(self.lineEdit.text())
        self.lineEdit_3.setText(data_3)

    def pushButton_4_func(self):
        data_4 = getRam(self.lineEdit.text())
        self.lineEdit_4.setText(data_4)

    def pushButton_5_func(self):
        data_5 = getFlow(self.lineEdit.text())
        self.lineEdit_5.setText(data_5)

    def pushButton_6_func(self):
        #设置新的阈值
        self.cpumax = self.lineEdit_6.text()
        #cpunow = getCPU(self.lineEdit.text())
        #cpunow = cpunow.strip('%')
        # QMessageBox.warning(self, "警告", "当前CPU占用过多", QMessageBox.Cancel)
        #self.lineEdit_5.setText(data_5)

    def operate(self):
        if self.lineEdit.text() != '':
            self.cpunow = getCPU(self.lineEdit.text())
            self.cpunow = self.cpunow.strip('%')
        if (self.cpumax < self.cpunow):
            QMessageBox.warning(self, "警告", "当前CPU占用过多", QMessageBox.Cancel)
        print("执行了一次")

class Mywidget(QWidget, Ui_Form):
    # 定义信号
    signal = pyqtSignal(str)
    def __init__(self, parent=None):
        super(Mywidget, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.slot)


    def slot(self):
        # 发射信号
        data = self.lineEdit.text()
        self.signal.emit(data)
        # 输入框清空
        self.lineEdit.setText("")
        # 显示主窗口
        mywin.show()
        # 关闭子窗口
        self.close()
        # 连接信号
        #mywidget.signal.connect(self.getData)
        #self.close()  # 关闭主界面



if __name__=="__main__":
    app = QApplication(sys.argv)
    mywin = Mymainwindow()
    mywidget = Mywidget()
    mywin.show()
    #mywidget.show()
    #mywin.pushButton.clicked.connect(mywidget.show)
    sys.exit(app.exec_())