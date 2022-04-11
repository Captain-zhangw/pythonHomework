from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QGraphicsView, QGraphicsScene, \
    QGraphicsPolygonItem
from PyQt5.QtGui import QPainter, QPolygon, QPen, QColor, QBrush, QPolygonF
from PyQt5.QtCore import QPointF, QRectF, Qt
import sys


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
        self.initUI()

    def initUI(self):
        self.setFixedSize(1200, 800)
        self.move(400, 100)
        self.setWindowTitle('Tangram')
        self.addButton()
        self.addTangram()

    def addButton(self):
        button1 = QPushButton("OK")
        button2 = QPushButton("cancel")
        button1.clicked.connect(self.buttonOKClicked)
        button2.clicked.connect(self.buttonCancelClicked)
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(button1)
        hbox.addWidget(button2)
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

    def addTangram(self):
        scene = GraphicsScene(self)
        # 刷子颜色
        brush1 = QBrush(QColor(0, 255, 255))
        brush2 = QBrush(QColor(255, 0, 0))
        brush3 = QBrush(QColor(255, 0, 255))
        brush4 = QBrush(QColor(0, 255, 0))
        brush5 = QBrush(QColor(128, 128, 255))
        brush6 = QBrush(QColor(255, 255, 0))
        brush7 = QBrush(QColor(255, 128, 68))
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
        item1.setBrush(brush1)
        item2.setBrush(brush2)
        item3.setBrush(brush3)
        item4.setBrush(brush4)
        item5.setBrush(brush5)
        item6.setBrush(brush6)
        item7.setBrush(brush7)
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
        view.resize(self.width() - 200, self.height())
        view.show()
        self.show()

    def buttonOKClicked(self):
        print("i am pressed")

    def buttonCancelClicked(self):
        print("close")
    # def paintEvent(self, e):
    #     qp=QPainter()
    #     qp.begin(self)
    #     col = QColor(0, 0, 0)
    #     qp.setBrush(QColor(200, 0, 0))
    #     triangle=QPolygon()
    #     triangle.setPoints(200,200,100,300,300,300)
    #     qp.drawPolygon(triangle)
    #     qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Tangram()
    sys.exit(app.exec_())
