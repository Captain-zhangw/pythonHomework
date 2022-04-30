import sys

import matplotlib
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QRectF, QTimerEvent
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene
from matplotlib import pyplot
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from ui.uiplot import Ui_MainWindow

matplotlib.use("Qt5Agg")
pyplot.rcParams['font.sans-serif'] = ['SimHei']
pyplot.rcParams['axes.unicode_minus'] = False


class NotEqualLengthError(Exception):
    def __init__(self, message):
        super(NotEqualLengthError, self).__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.graphicsScene = QGraphicsScene(self)
        self.F = FigureCanvasQTAgg(Figure(figsize=(5, 4), dpi=100))
        self.paint = None
        self.sum = 0
        self.x1 = []
        self.y1 = []
        self.x2 = []
        self.y2 = []
        self.setMinimumHeight(810)
        self.setMaximumHeight(900)
        self.initUi()
        self.timer = self.startTimer(200)
        self.show()

    def initUi(self):
        self.xAxislineEdit.hide()
        self.yAxisLineEdit.hide()
        self.yAxisName.hide()
        self.xAxisName.hide()
        self.legendCheckBox.setChecked(True)
        # 将画图添加到窗口中
        self.paint = self.F.figure.add_subplot(111)
        width, height = self.graphicsView.width(), self.graphicsView.height()
        self.F.resize(width - 30, height - 30)
        # 如果标题复选框被选中，则标题可编辑，否则不可编辑
        self.titleCheckBox.stateChanged.connect(self.showTitle)
        # 点击清除标题按钮，清除标题
        self.titleClearButton.clicked.connect(self.clearTitle)
        # 如果轴标题复选框被选中，则轴标题显示，否则不显示
        self.axisTitleCheckBox.stateChanged.connect(self.showAxisTitle)
        # 如果图例复选框被选中，则图例可编辑，否则不可编辑
        self.legendCheckBox.stateChanged.connect(self.showLegend)
        # 输入数据后，更新图表
        self.insertDataButton.clicked.connect(self.updatePlot)
        # 绘图
        self.graphicsView.setScene(self.graphicsScene)
        self.graphicsScene.addWidget(self.F)

    def showTitle(self):
        if self.titleCheckBox.isChecked():
            self.titleEdit.setEnabled(True)
            self.titleClearButton.setEnabled(True)
        else:
            self.titleEdit.setEnabled(False)
            self.titleClearButton.setEnabled(False)

    def updatePlot(self):
        self.x1 = []
        self.y1 = []
        self.x2 = []
        self.y2 = []
        self.paint.clear()
        if self.xAxisData.toPlainText() != "":
            try:
                x1 = self.xAxisData.toPlainText().split('\n')
                y1 = self.yAxisData.toPlainText().split('\n')
                for i, j in zip(x1, y1):
                    if i == "" or i == " " or i == "\n":
                        pass
                    else:
                        self.x1.append(float(i))
                    if j == "" or j == " " or j == "\n":
                        pass
                    else:
                        self.y1.append(float(j))
                if len(self.x1) != len(self.y1):
                    ex = NotEqualLengthError("数据1中的x轴数据与y轴数据长度不一致")
                    raise ex
            except NotEqualLengthError as e:
                print(e.message)
            except ValueError:
                print("数据1中的输入的数据不是数字")
            else:
                self.plotWithPoint(self.x1, self.y1, self.data1LegendLineEdit.text(), 1)
        if self.x2AxisData.toPlainText() != "":
            try:
                x2 = self.x2AxisData.toPlainText().split('\n')
                y2 = self.y2AxisData.toPlainText().split('\n')
                for i, j in zip(x2, y2):
                    if i == "" or i == " " or i == "\n":
                        pass
                    else:
                        self.x2.append(float(i))
                    if j == "" or j == " " or j == "\n":
                        pass
                    else:
                        self.y2.append(float(j))
                if len(self.x2) != len(self.y2):
                    ex = NotEqualLengthError("数据2中的x轴数据与y轴数据长度不一致")
                    raise ex
            except NotEqualLengthError as e:
                print(e.message)
            except ValueError:
                print("数据2中的输入的数据不是数字")
            else:
                self.plotWithPoint(self.x2, self.y2, self.data1LegendLineEdit.text(), 2)

        if self.legendCheckBox.isChecked():
            self.paint.legend(loc='best')
        self.F.draw()

    def plotWithPoint(self, x, y, legend, pos):
        if pos == 1:
            if self.data1WithLine.isChecked():
                if self.radiusRadio.isChecked():
                    self.paint.plot(x, y, 'o-', label=legend)
                if self.triangleRadio.isChecked():
                    self.paint.plot(x, y, 'v-', label=legend)
                if self.rectRadio.isChecked():
                    self.paint.plot(x, y, 's-', label=legend)
                if self.plusRadio.isChecked():
                    self.paint.plot(x, y, '+-', label=legend)
                if self.mutiplyRadio.isChecked():
                    self.paint.plot(x, y, 'x-', label=legend)
                if self.pentagonRadio.isChecked():
                    self.paint.plot(x, y, 'p-', label=legend)
                if self.rhombusRadio.isChecked():
                    self.paint.plot(x, y, 'd-', label=legend)
                if self.starRadio.isChecked():
                    self.paint.plot(x, y, '*-', label=legend)
            else:
                if self.radiusRadio.isChecked():
                    self.paint.plot(x, y, 'o', label=legend)
                if self.triangleRadio.isChecked():
                    self.paint.plot(x, y, 'v', label=legend)
                if self.rectRadio.isChecked():
                    self.paint.plot(x, y, 's', label=legend)
                if self.plusRadio.isChecked():
                    self.paint.plot(x, y, '+', label=legend)
                if self.mutiplyRadio.isChecked():
                    self.paint.plot(x, y, 'x', label=legend)
                if self.pentagonRadio.isChecked():
                    self.paint.plot(x, y, 'p', label=legend)
                if self.rhombusRadio.isChecked():
                    self.paint.plot(x, y, 'd', label=legend)
                if self.starRadio.isChecked():
                    self.paint.plot(x, y, '*', label=legend)
        if pos == 2:
            if self.data2WithLine.isChecked():
                if self.radiusRadio_3.isChecked():
                    self.paint.plot(x, y, 'o-', label=legend)
                if self.triangleRadio_3.isChecked():
                    self.paint.plot(x, y, 'v-', label=legend)
                if self.rectRadio_3.isChecked():
                    self.paint.plot(x, y, 's-', label=legend)
                if self.plusRadio_3.isChecked():
                    self.paint.plot(x, y, '+-', label=legend)
                if self.mutiplyRadio_3.isChecked():
                    self.paint.plot(x, y, 'x-', label=legend)
                if self.pentagonRadio_3.isChecked():
                    self.paint.plot(x, y, 'p-', label=legend)
                if self.rhombusRadio_3.isChecked():
                    self.paint.plot(x, y, 'd-', label=legend)
                if self.starRadio_3.isChecked():
                    self.paint.plot(x, y, '*-', label=legend)
            else:
                if self.radiusRadio_3.isChecked():
                    self.paint.plot(x, y, 'o', label=legend)
                if self.triangleRadio_3.isChecked():
                    self.paint.plot(x, y, 'v', label=legend)
                if self.rectRadio_3.isChecked():
                    self.paint.plot(x, y, 's', label=legend)
                if self.plusRadio_3.isChecked():
                    self.paint.plot(x, y, '+', label=legend)
                if self.mutiplyRadio_3.isChecked():
                    self.paint.plot(x, y, 'x', label=legend)
                if self.pentagonRadio_3.isChecked():
                    self.paint.plot(x, y, 'p', label=legend)
                if self.rhombusRadio_3.isChecked():
                    self.paint.plot(x, y, 'd', label=legend)
                if self.starRadio_3.isChecked():
                    self.paint.plot(x, y, '*', label=legend)

    def showLegend(self):
        if self.legendCheckBox.isChecked():
            self.data1LegendName.show()
            self.data1LegendLineEdit.show()
            self.data2LegendName.show()
            self.data2LegendLineEdit.show()
        else:
            self.data1LegendName.hide()
            self.data1LegendLineEdit.hide()
            self.data2LegendName.hide()
            self.data2LegendLineEdit.hide()

    def showAxisTitle(self):
        if self.axisTitleCheckBox.isChecked():
            self.xAxislineEdit.show()
            self.xAxisName.show()
            self.yAxisLineEdit.show()
            self.yAxisName.show()
        else:
            self.xAxislineEdit.hide()
            self.yAxisLineEdit.hide()
            self.yAxisName.hide()
            self.xAxisName.hide()

    def clearTitle(self):
        self.titleEdit.clear()

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QPainter(self)
        painter.setPen(Qt.red)
        painter.setFont(QtGui.QFont("Times", 22))
        windowTitleRect = QRectF(self.width() // 2 - 45, 40, 120, 120)
        painter.drawText(windowTitleRect, "自动作图")

    def timerEvent(self, a0: 'QTimerEvent') -> None:
        if a0.timerId() == self.timer:
            if self.titleCheckBox.isChecked():
                self.paint.set_title(self.titleEdit.text())
            else:
                self.paint.set_title("")
            if self.gridCheckBox.isChecked():
                self.paint.grid(True)
            else:
                self.paint.grid(False)
            if self.axisTitleCheckBox.isChecked():
                self.paint.set_xlabel(self.xAxislineEdit.text())
                self.paint.set_ylabel(self.yAxisLineEdit.text())
            else:
                self.paint.set_xlabel("")
                self.paint.set_ylabel("")
            self.F.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
