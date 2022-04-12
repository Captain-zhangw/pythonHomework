from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QGraphicsView, QGraphicsScene, \
    QGraphicsPolygonItem, QFileDialog, QMessageBox
from PyQt5.QtGui import QPen, QColor, QBrush, QPolygonF, QMouseEvent, QPainter, QFont, QPixmap
from PyQt5.QtCore import QPointF, Qt, QRectF
import sys


class PushButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("QPushButton{background-color:"
                           "#f5f6fa;color:#2f3640;"
                           "font-size:15pt'微软雅黑';border-radius:15px;"
                           "border-style:solid;border-width:2px;"
                           "padding:8px;}"
                           "QPushButton::hover{	color: #FFFFFF;"
                           "background-color: #718093;border-color: #2f3640;}"
                           "QPushButton::pressed,QPushButton::checked{color: #FFFFFF;"
                           "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #273c75, stop:1 #487eb0);}"
                           )


class GraphicsPolygonItem(QGraphicsPolygonItem):
    def __init__(self, polygon, parent=None):
        QGraphicsPolygonItem.__init__(self, polygon, parent)
        self.setTransformOriginPoint(0, 50)
        self.setPen(QPen(QColor(0, 0, 0), 1))
        self.setAcceptDrops(True)
        self.mouse_press_pos = None
        self.mouse_press_rect_pos = None

    # def mousePressEvent(self, event):
    # self.setRotation(self.rotation()+45)

    def mousePressEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
        if event.button() == Qt.LeftButton:
            self.mouse_press_pos = event.scenePos()
            self.mouse_press_rect_pos = self.pos()
        else:
            self.setRotation(self.rotation() + 45)

    def mouseMoveEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
        if event.buttons() == Qt.LeftButton:
            if -400 <= self.mouse_press_rect_pos.x() + event.scenePos().x() - self.mouse_press_pos.x() <= 400 and -200 <= self.mouse_press_rect_pos.y() + event.scenePos().y() - self.mouse_press_pos.y() <= 400:
                self.setPos(self.mouse_press_rect_pos + event.scenePos() - self.mouse_press_pos)
            else:
                print("out of range")
    # def dragMoveEvent(self, event: 'QGraphicsSceneDragDropEvent') -> None:
    #     print("dragMoveEvent")
    #     self.setPos(event.scenePos())
    #     self.update()


class GraphicsScene(QGraphicsScene):
    def __init__(self, parent=None):
        QGraphicsScene.__init__(self, parent)
        self.setSceneRect(1200, 600, 0, 0)
        self.opt = ""

    # def mousePressEvent(self, event):
    #     print("I am pressed")


class Tangram(QWidget):
    def __init__(self):
        super().__init__()
        self.scene = GraphicsScene()
        self.view = QGraphicsView()
        self.brush1 = QBrush(QColor(0, 255, 255))
        self.brush2 = QBrush(QColor(255, 0, 0))
        self.brush3 = QBrush(QColor(255, 0, 255))
        self.brush4 = QBrush(QColor(0, 255, 0))
        self.brush5 = QBrush(QColor(128, 128, 255))
        self.brush6 = QBrush(QColor(255, 255, 0))
        self.brush7 = QBrush(QColor(255, 128, 68))
        self.initUI()

    def initUI(self):
        self.setFixedSize(1200, 800)
        self.move(400, 100)
        self.setWindowTitle('Tangram')
        self.addButton()
        self.addTangram()

    def addButton(self):
        button1 = PushButton("读取格式")
        button2 = PushButton("保存格式")
        button3 = PushButton("保存图片")
        button1.clicked.connect(self.buttonReadClicked)
        button2.clicked.connect(self.buttonSaveClicked)
        button3.clicked.connect(self.buttonImgClicked)
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        vbox.addStretch(3)
        vbox.addWidget(button1)
        vbox.addStretch(1)
        vbox.addWidget(button2)
        vbox.addStretch(1)
        vbox.addWidget(button3)
        vbox.addStretch(3)
        hbox.addStretch(1)
        hbox.addLayout(vbox)
        self.setLayout(hbox)

    def addTangram(self):
        scene = GraphicsScene(self)
        self.scene = scene
        # 刷子颜色
        # 创建图形W
        rect = QPolygonF([QPointF(0, 0), QPointF(0, 70.5), QPointF(70.5, 70.5), QPointF(70.5, 0)])
        points = [QPointF(50, 0), QPointF(0, 50), QPointF(100, 50)]
        points2 = [QPointF(100, 0), QPointF(0, 100), QPointF(200, 100)]
        points3 = [QPointF(70.5, 0), QPointF(0, 70.5), QPointF(141, 70.5)]
        points4 = [QPointF(50, 0), QPointF(150, 0), QPointF(100, 50), QPointF(0, 50)]
        triangle1 = QPolygonF(points)
        triangle2 = QPolygonF(points)
        triangle3 = QPolygonF(points2)
        triangle4 = QPolygonF(points2)
        triangle5 = QPolygonF(points3)
        trapezoid = QPolygonF(points4)
        # 加入到scene
        item1 = GraphicsPolygonItem(triangle1)
        item2 = GraphicsPolygonItem(triangle2)
        item3 = GraphicsPolygonItem(triangle3)
        item4 = GraphicsPolygonItem(triangle4)
        item5 = GraphicsPolygonItem(triangle5)
        item6 = GraphicsPolygonItem(trapezoid)
        item7 = GraphicsPolygonItem(rect)
        item1.setBrush(self.brush1)
        item2.setBrush(self.brush2)
        item3.setBrush(self.brush3)
        item4.setBrush(self.brush4)
        item5.setBrush(self.brush5)
        item6.setBrush(self.brush6)
        item7.setBrush(self.brush7)
        item1.setData(0, "triangle1")
        item2.setData(0, "triangle2")
        item3.setData(0, "triangle3")
        item4.setData(0, "triangle4")
        item5.setData(0, "triangle5")
        item6.setData(0, "trapezoid")
        item7.setData(0, "rect")
        scene.addItem(item1)
        scene.addItem(item2)
        scene.addItem(item3)
        scene.addItem(item4)
        scene.addItem(item5)
        scene.addItem(item6)
        scene.addItem(item7)
        # 设置位置
        item1.setPos(0, 0)
        item2.setPos(0, 50)
        item3.setPos(0, 100)
        item4.setPos(0, 150)
        item5.setPos(0, 200)
        item6.setPos(0, 250)
        item7.setPos(0, 300)
        # item1.setTransformOriginPoint(QPointF(50, 0))
        # item1.setRotation(45)
        # 将scene添加到view
        scene.setSceneRect(self.width() - 200, self.height(), 0, 0)
        view = QGraphicsView(scene, self)
        self.view = view
        view.resize(self.width() - 200, self.height())
        view.show()

    def closeEvent(self, a0) -> None:

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
            a0.accept()
        else:
            a0.ignore()

    def buttonReadClicked(self):
        file_name = QFileDialog.getOpenFileNames(self, '打开文件', './', '*.txt')
        try:
            if file_name[0]:
                saved_txt = open(str(file_name[0][0]), 'r', encoding='utf-8')
                mes = saved_txt.readlines()
                pos_mes = mes[::2]
                pos_mes_x = []
                pos_mes_y = []
                for i in pos_mes:
                    pos_mes_x.append(i.split(" ")[0])
                    pos_mes_y.append(i.split(" ")[1][:-1])
                rotation_mes = mes[1::2]
                for i in range(0, len(rotation_mes)):
                    rotation_mes[i] = rotation_mes[i][:-1]
                for i, j in zip(range(0, len(self.scene.items())), range(0, len(self.scene.items()))):
                    self.scene.items()[i].setPos(float(pos_mes_x[j]), float(pos_mes_y[j]))
                    self.scene.items()[i].setRotation(float(rotation_mes[j]))
                saved_txt.close()
            else:
                return
        except:
            print("wrong file format!")

    def buttonSaveClicked(self):
        file_name = QFileDialog.getSaveFileName(self, '保存文件', './', '文本文件(*.txt)', 'save')
        if file_name[0]:
            print(file_name[0])
            save_txt = open(file_name[0], 'w+', encoding='UTF-8')
            for i in self.scene.items():
                save_txt.write(str(i.pos().x()) + ' ' + str(i.pos().y()) + '\n')
                save_txt.write(str(i.rotation()) + '\n')
            save_txt.close()

    def buttonImgClicked(self):
        rect = QGraphicsView.viewport(self.view).rect()
        pixmap = QPixmap(rect.width(), rect.height())
        painter = QPainter(pixmap)
        painter.begin(pixmap)
        self.view.render(painter, QRectF(pixmap.rect()), rect)
        painter.end()
        file_name = QFileDialog.getSaveFileName(self, '保存图片', './', '图片(*.png)')
        if file_name[0]:
            pixmap.save(file_name[0])


class HelpWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.w = Tangram()

    def initUI(self):
        self.setFixedSize(1200, 800)
        self.move(400, 100)
        self.setWindowTitle('TangramHelp')
        self.show()

    def mousePressEvent(self, a0: QMouseEvent) -> None:
        if a0.button() == Qt.LeftButton:
            print("I am pressed")
            self.w.show()
            self.close()

    def paintEvent(self, a0) -> None:
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 15, Qt.SolidLine))
        painter.setFont(QFont("楷体", 30))
        painter.drawText(0, 0, int(self.width()), int(self.height() / 2 - 100), Qt.AlignCenter, "欢迎来到Tangram——七巧板！")
        painter.setFont(QFont("楷体", 20))
        painter.drawText(0, 0, int(self.width()), int(self.height() / 2 + 200), Qt.AlignCenter, "下面让我来介绍一下七巧板的基本操作：")
        painter.drawText(0, 0, int(self.width()), int(self.height() / 2 + 300), Qt.AlignCenter,
                         "使用鼠标左键拖拽改变图形的位置，右键点击改变图形的旋转角度")
        painter.drawText(0, 0, int(self.width()), int(self.height() / 2 + 400), Qt.AlignCenter,
                         "右面有三个按钮，分别是：保存格式、读取格式、保存图像")
        painter.drawText(0, 0, int(self.width()), int(self.height() / 2 + 500), Qt.AlignCenter,
                         "以txt格式保存格式，读取格式，可以使你的七巧板读取到你之前保存的格式")
        painter.drawText(0, 0, int(self.width()), int(self.height() / 2 + 600), Qt.AlignCenter, "保存图像，可以使你的七巧板保存到你的电脑中")
        painter.setPen(QPen(Qt.red, 15, Qt.SolidLine))
        painter.setFont(QFont("楷体", 25))
        painter.drawText(0, 0, int(self.width()), int(self.height() / 2 + 800), Qt.AlignCenter, "左键点击屏幕，进入七巧板")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    HelpWidget = HelpWidget()
    sys.exit(app.exec_())
