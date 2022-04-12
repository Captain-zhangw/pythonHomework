# 基于Qt实现的七巧板

## 环境要求

---

```python
pip install pyqt5
```

## 开发流程

---

### 前期准备

- 需要利用到的`pyqt`模块
  - `QGraphicsView`
    - 用于观察scene中的图像
  - ` QGraphicsScene`
    - 在scene中添加item来形成七巧板
  - `QGraphicsPolygonItem`
    - 七巧板中各种图形的实体，包括矩形、平行四边形、三角形
- 设计思想
  - 首先产生一个继承于`QWidget`的新类`Tangram`，在此基础上添加以上提到的`pyqt`模块，使得在此类中可以产生七巧板的基本内容

### 添加七巧板

- 所有七巧板选用的均为`Polygon`类型
- 不同七巧板选用不同的`Qbrush`,选取不同的颜色`QColor`
- 设置不同的起始位置

### 添加事件

- 添加鼠标移动事件来使得鼠标拖动可以改变七巧板的位置
- 添加鼠标右键点击事件使得鼠标右键可以进行选择、
- 判断鼠标移动的位置，使得七巧板不能出界

### 添加按钮

- 添加了保存按钮
- 添加了读取按钮
- 添加了保存图像按钮

### 后期完善

- 为了使得用户可以了解规则，新增了一个`	HelpWidget`界面，提供帮助操作信息，左键点击后可以跳转到主界面
- 重写了主界面的关闭事件，点击关闭时会进行提醒先进行保存后再退出
- 增加了三个`txt`文件，提供了七巧板可以拼成的三个基本图形

## 效果展示	

---

![image-20220412112102068](F:\学习\Python程序设计\code\image\1.png)

![image-20220412112140019](F:\学习\Python程序设计\code\image\2.png)

![image-20220412112202776](C:\Users\Brezze\AppData\Roaming\Typora\typora-user-images\image-20220412112202776.png)

![image-20220412112217768](C:\Users\Brezze\AppData\Roaming\Typora\typora-user-images\image-20220412112217768.png)
