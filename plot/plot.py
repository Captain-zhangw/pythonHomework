import sys

import matplotlib
import numpy as np
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QFileDialog, QMessageBox, QPushButton
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
        self.savedFigure = 1
        self.setWindowIcon(QtGui.QIcon('./icon/icon.ico'))
        self.setMinimumHeight(940)
        self.setMaximumHeight(950)
        self.initUi()
        self.show()

    def initUi(self):
        self.xAxislineEdit.hide()
        self.yAxisLineEdit.hide()
        self.yAxisName.hide()
        self.xAxisName.hide()
        self.legendCheckBox.setChecked(True)
        # 将画图添加到窗口中
        self.paint = self.F.figure.add_subplot(111)
        self.F.figure.subplots_adjust(left=0.15, bottom=0.15, right=0.85, top=0.85)
        self.paint.set_title(self.titleEdit.text(), fontsize=20, y=1.02)
        width, height = self.graphicsView.width(), self.graphicsView.height()
        self.F.resize(width, height - 30)
        # 如果标题复选框被选中，则标题可编辑，否则不可编辑
        self.titleCheckBox.stateChanged.connect(self.showTitle)
        # 点击清除标题按钮，清除标题
        self.titleClearButton.clicked.connect(self.clearTitle)
        # 如果轴标题复选框被选中，则轴标题显示，否则不显示
        self.axisTitleCheckBox.stateChanged.connect(self.showAxisTitle)
        # 如果图例复选框被选中，则图例可编辑，否则不可编辑
        self.legendCheckBox.stateChanged.connect(self.showLegend)
        # 输入数据后，绘制图表
        self.insertDataButton.clicked.connect(self.drawPlot)
        # 更改数据标签选项，更新图表
        self.dataCheckBox.stateChanged.connect(self.updatePlot)
        # 更改坐标轴标签选项，更新图表
        self.axisTitleCheckBox.stateChanged.connect(self.updatePlot)
        self.xAxislineEdit.textChanged.connect(self.updatePlot)
        self.yAxisLineEdit.textChanged.connect(self.updatePlot)
        # 更改网格选项，更新图表
        self.gridCheckBox.stateChanged.connect(self.updatePlot)
        # 更改标题名称，更新图表
        self.titleEdit.textChanged.connect(self.updatePlot)
        # 绑定单选框事件,更改标记形状，重绘图表
        self.radiusRadio.toggled.connect(self.updatePlot)
        self.rectRadio.toggled.connect(self.updatePlot)
        self.plusRadio.toggled.connect(self.updatePlot)
        self.triangleRadio.toggled.connect(self.updatePlot)
        self.starRadio.toggled.connect(self.updatePlot)
        self.mutiplyRadio.toggled.connect(self.updatePlot)
        self.pentagonRadio.toggled.connect(self.updatePlot)
        self.rhombusRadio.toggled.connect(self.updatePlot)
        self.radiusRadio_3.toggled.connect(self.updatePlot)
        self.rectRadio_3.toggled.connect(self.updatePlot)
        self.plusRadio_3.toggled.connect(self.updatePlot)
        self.triangleRadio_3.toggled.connect(self.updatePlot)
        self.starRadio_3.toggled.connect(self.updatePlot)
        self.mutiplyRadio_3.toggled.connect(self.updatePlot)
        self.pentagonRadio_3.toggled.connect(self.updatePlot)
        self.rhombusRadio_3.toggled.connect(self.updatePlot)
        # 线性拟合事件
        self.actionLineFitting.triggered.connect(self.lineFitting)
        # 二次拟合事件
        self.actionQuaFitting.triggered.connect(self.quaFitting)
        # 更改拟合结果，更新图标
        self.fittingResCheckBox.stateChanged.connect(self.fitting)
        # 绘图
        self.graphicsView.setScene(self.graphicsScene)
        self.graphicsScene.addWidget(self.F)
        # 保存图片事件
        self.actionSavePic.triggered.connect(self.saveFigure)
        # 添加查看帮助
        self.actionCheckHelp.triggered.connect(self.showHelp)

    def showTitle(self):
        if self.titleCheckBox.isChecked():
            self.titleEdit.setEnabled(True)
            self.titleClearButton.setEnabled(True)
        else:
            self.titleEdit.setEnabled(False)
            self.titleClearButton.setEnabled(False)

    def drawPlot(self):
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
                print(len(self.x1), len(self.y1))
            except NotEqualLengthError as e:
                QMessageBox.warning(self, "警告", e.message)
            except ValueError:
                QMessageBox.warning(self, "警告", "数据1中的输入的数据不是数字")
            except:
                QMessageBox.warning(self, "警告", "数据1中的输入的数据不合法")
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
                QMessageBox.warning(self, "警告", e.message)
            except ValueError:
                QMessageBox.warning(self, "警告", "数据2中的输入的数据不是数字")
            except:
                QMessageBox.warning(self, "警告", "数据2中的输入的数据不合法")
            else:
                self.plotWithPoint(self.x2, self.y2, self.data1LegendLineEdit.text(), 2)

        if self.legendCheckBox.isChecked():
            self.paint.legend(loc='best')
        self.gridCheckBox.stateChanged.emit(1)
        self.F.draw()

    def updatePlot(self):
        self.paint.clear()
        if self.dataCheckBox.isChecked():
            self.plotWithPoint(self.x1, self.y1, self.data1LegendLineEdit.text(), 1)
            self.plotWithPoint(self.x2, self.y2, self.data2LegendLineEdit.text(), 2)
            for i, j in zip(self.x1, self.y1, ):
                self.paint.text(i, j + 0.04, '%.0f' % j, ha='center', va='bottom', fontsize=9)
            for i, j in zip(self.x2, self.y2, ):
                self.paint.text(i, j + 0.04, '%.0f' % j, ha='center', va='bottom', fontsize=9)
        elif not self.dataCheckBox.isChecked():
            self.plotWithPoint(self.x1, self.y1, self.data1LegendLineEdit.text(), 1)
            self.plotWithPoint(self.x2, self.y2, self.data2LegendLineEdit.text(), 2)
            if self.legendCheckBox.isChecked():
                self.paint.legend(loc='best')
        if self.gridCheckBox.isChecked():
            self.paint.grid(True)
        else:
            self.paint.grid(False)
        if self.axisTitleCheckBox.isChecked():
            self.paint.set_xlabel(self.xAxislineEdit.text(), fontsize=14, y=1.5)
            self.paint.set_ylabel(self.yAxisLineEdit.text(), fontsize=14)
        else:
            self.paint.set_xlabel("")
            self.paint.set_ylabel("")
        if self.titleCheckBox.isChecked():
            self.paint.set_title(self.titleEdit.text(), fontsize=20, y=1.02)
        else:
            self.paint.set_title("")
        if self.fittingResCheckBox.isChecked():
            self.fitting()
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

    def lineFitting(self):
        if self.fittingResCheckBox.isChecked():
            if self.actionLineFitting.isChecked():
                try:
                    f1 = np.polyfit(np.array(self.x1), np.array(self.y1), 1)
                    p1 = np.poly1d(f1)
                    print()
                    self.paint.plot(self.x1, p1(self.x1), label=p1.__str__())
                    if self.legendCheckBox.isChecked():
                        self.paint.legend()
                except:
                    pass
                try:
                    f2 = np.polyfit(self.x2, self.y2, 1)
                    p2 = np.poly1d(f2)
                    self.paint.plot(self.x2, p2(self.x2), label=p2.__str__())
                    if self.legendCheckBox.isChecked:
                        self.paint.legend()
                except:
                    pass
                self.F.draw()
            elif not self.actionLineFitting.isChecked():
                self.updatePlot()
            self.F.draw()
        else:
            self.updatePlot()

    def quaFitting(self):
        if self.fittingResCheckBox.isChecked():
            if self.actionQuaFitting.isChecked():
                try:
                    f1 = np.polyfit(self.x1, self.y1, 2)
                    p1 = np.poly1d(f1)
                    px1 = np.linspace(min(self.x1), max(self.x1), 100)
                    self.paint.plot(px1, p1(px1), label=p1.__str__())
                    if self.legendCheckBox.isChecked:
                        self.paint.legend()
                except:
                    pass
                try:
                    f2 = np.polyfit(self.x2, self.y2, 2)
                    p2 = np.poly1d(f2)
                    px2 = np.linspace(min(self.x2), max(self.x2), 100)
                    self.paint.plot(px2, p2(px2), label=p2.__str__())
                    if self.legendCheckBox.isChecked:
                        self.paint.legend()
                except:
                    pass
                self.F.draw()
            elif not self.actionQuaFitting.isChecked():
                self.updatePlot()
                if self.actionLineFitting.isChecked():
                    self.lineFitting()

    def fitting(self):
        if self.fittingResCheckBox.isChecked():
            if self.actionLineFitting.isChecked():
                self.lineFitting()
            if self.actionQuaFitting.isChecked():
                self.quaFitting()
        else:
            self.updatePlot()

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
        windowTitleRect = QRectF(self.width() // 2 - 45, 40, 150, 150)
        painter.drawText(windowTitleRect, "自动作图")

    def saveFigure(self):
        filename = QFileDialog.getSaveFileName(self, '保存文件', './Figure' + str(self.savedFigure), '*.png;;*.jpg;')
        print(filename)
        if filename[0]:
            self.paint.figure.savefig(filename[0])
            self.savedFigure += 1

    def showHelp(self):
        QMessageBox.information(self, "帮助",
                                "1.在左侧数据框中输入x和y的数据，每个数据间使用回车分割\n2.输入数据并选择图例和标记类型后点击输入数据即可生成图形\n"
                                "3.在左上角选项中可以选择进行线性拟合或者二次拟合，选择后点击下方的拟合结果即可输出拟合结果\n4.在选项中点击保存图片即可保存图片")

    def closeEvent(self, event):
        close_sure = QMessageBox(self)
        close_sure.setWindowTitle("提示")
        close_sure.setText("确定要退出吗？,退出之前记得保存哦！")
        btn1 = QPushButton("确定")
        btn2 = QPushButton("取消")
        close_sure.addButton(btn1, QMessageBox.YesRole)
        close_sure.addButton(btn2, QMessageBox.NoRole)
        close_sure.setDefaultButton(btn2)
        close_sure.setIcon(QMessageBox.Question)
        close_sure.exec_()
        if close_sure.clickedButton() == btn1:
            event.accept()
        else:
            event.ignore()


class Controller(QMainWindow):
    def __init__(self):
        super(Controller, self).__init__()
        self.plotWidget = []
        self.plotWidget.append(MainWindow())
        self.plotWidget[0].actionCreatNewFile.triggered.connect(self.createNewFile)
        self.plotWidget[0].show()

    def createNewFile(self):
        self.plotWidget.append(MainWindow())
        self.plotWidget[-1].actionCreatNewFile.triggered.connect(self.createNewFile)
        self.plotWidget[-1].setGeometry(window.width() // 2 + 110,
                                        window.height() // 2 - 150 + 20 * len(self.plotWidget), 1068, 764)
        self.plotWidget[-1].show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Controller()
    sys.exit(app.exec_())
