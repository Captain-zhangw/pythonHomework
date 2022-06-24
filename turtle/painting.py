from turtle import *
import random
import math


# 作者：Captainzw
def paint():
    TREEX = -150
    TREEWIDTH = 45
    BRANCHNUM = 5
    BRANCHSUM = 35
    colorlist = ['#99bf40', '#4db357', '#c7f709', '#80ee11', '#aa55aa', '#04b0fb']
    tracer(False)

    setup(1200, 600)

    def fish():
        setheading(0)
        setheading(90)
        pendown()
        a = 0.5
        for i in range(1, 72):
            if 0 <= i < 18 or 36 <= i < 54:
                a = a + 0.1
                left(5)
                forward(a)
            else:
                a = a - 0.1
                left(5)
                forward(a)
        setheading(30)
        forward(12)
        setheading(270)
        forward(12)
        setheading(150)
        forward(12)
        setheading(175)
        penup()
        forward(25)
        pendown()
        circle(2, 360, 100)

    def branch(num):
        if int(num) == int(BRANCHNUM):
            return
        pensize((BRANCHNUM - num) * 1.5)
        pencolor(colorlist[num - 1])
        if num != 1:
            head = heading()
            setheading(head + math.floor(52 * random.uniform(-1, 1)))
        for i in range(1, BRANCHNUM):
            pencolor(colorlist[num - 1])
            pensize((BRANCHNUM - num) * 1.5)
            forward(30 // num + 5 * random.random())
            x = xcor()
            y = ycor()
            head = heading()
            branch(num + 1)
            penup()
            setposition(x, y)
            setheading(head)
            pendown()
        if num != BRANCHNUM - 1:
            forward(30 // num + 60 // num * random.random())

    # 树干
    speed(0)
    penup()
    setpos(TREEX - 20, -window_height() / 2 + 20)
    setheading(90)
    pendown()
    fillcolor('#804040')
    pencolor('black')
    begin_fill()
    forward(260)
    right(90)
    forward(TREEWIDTH)
    right(90)
    forward(260)
    right(90)
    forward(TREEWIDTH)
    end_fill()

    # 树枝
    for i in range(1, BRANCHSUM - 1):
        penup()
        setpos(TREEX + (i - BRANCHSUM // 2) * 0.8, -window_height() / 2 + 200 + 20 * random.random())
        pendown()
        setheading(90 + (BRANCHSUM // 2 - i) * 4.2)
        branch(1)

    # 小猫

    # 猫头

    speed(0)
    penup()
    setpos(TREEX + TREEWIDTH // 2 + 10, -window_height() / 2 + 150)
    x = xcor()
    y = ycor()
    pendown()
    pencolor('orange')
    pensize(3)
    begin_fill()
    fillcolor('orange')
    setheading(15)
    circle(18, 360, 300)
    end_fill()
    x = x - 10
    y = y + 36
    penup()
    begin_fill()
    setpos(x, y)
    pendown()
    setheading(155)
    forward(13)
    setheading(275)
    forward(18)
    x = x + 20
    y = y - 8
    penup()
    setpos(x, y)
    pendown()
    setheading(75)
    forward(13)
    setheading(205)
    forward(18)
    end_fill()
    x = x - 23
    y = y - 10
    setheading(0)
    penup()
    setpos(x, y)
    pendown()
    pencolor('black')
    pensize(1)
    circle(5, 360, 100)
    y = y + 3
    x = x - 1
    penup()
    setpos(x, y)
    pendown()
    pensize(3)
    circle(2, 360, 100)
    y = y - 3
    x = x + 18
    penup()
    setpos(x, y)
    pendown()
    pensize(1)
    circle(5, 360, 100)
    y = y + 3
    x = x - 1
    penup()
    setpos(x, y)
    pendown()
    pensize(3)
    circle(2, 360, 100)
    x = x - 8
    y = y - 10
    penup()
    setpos(x, y)
    pendown()
    pensize(2)
    circle(1, 360, 100)
    setheading(270)
    forward(2)
    penup()
    x = xcor() + 2
    y = ycor()
    pensize(1)
    pendown()
    circle(2, 180, 100)
    penup()
    setpos(x - 7, y)
    pendown()
    setheading(270)
    circle(2, 180, 100)
    x = xcor()
    y = ycor()
    penup()
    setpos(x - 9, y + 2)
    pendown()
    setheading(160)
    forward(15)
    penup()
    setpos(x - 9, y)
    pendown()
    setheading(180)
    forward(15)
    penup()
    setpos(x - 9, y - 2)
    pendown()
    setheading(200)
    forward(15)
    penup()
    setpos(x + 9, y + 2)
    pendown()
    setheading(20)
    forward(15)
    penup()
    setpos(x + 9, y)
    pendown()
    setheading(0)
    forward(15)
    penup()
    setpos(x + 9, y - 2)
    pendown()
    setheading(340)
    forward(15)

    # 猫身
    penup()
    setpos(x - 9, y - 8)
    pendown()
    setheading(260)
    begin_fill()
    circle(350, 12, 500)
    penup()
    x = xcor()
    y = ycor()
    setpos(x + 36, y + 3)
    pendown()
    setheading(90)
    circle(349, 12, 500)
    setheading(180)
    pencolor('orange')
    forward(22)
    penup()
    setpos(x, y)
    pendown()
    pencolor('black')
    setheading(337)
    circle(35, 68, 200)
    end_fill()
    penup()
    setpos(x, y + 20)
    setheading(175)
    pendown()
    begin_fill()
    forward(16)
    circle(6, 180, 50)
    forward(19)
    end_fill()
    begin_fill()
    penup()
    setpos(x + 2, y + 65)
    setheading(175)
    pendown()
    begin_fill()
    forward(16)
    circle(6, 180, 50)
    forward(22)
    end_fill()

    # 猫尾
    penup()
    begin_fill()
    setpos(x + 25, y)
    pendown()
    setheading(290)
    circle(300, 6, 200)
    setheading(296)
    circle(5, 180, 200)
    circle(500, 4, 200)
    end_fill()

    # 鱼塘
    tracer(False)
    pencolor('black')
    penup()
    a = 1
    setpos(-TREEX + 200, -window_height() / 2 + 80)
    pendown()
    fillcolor('#00a2e8')
    begin_fill()
    setheading(90)
    for i in range(1, 120):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.3
            left(3)
            forward(a)
        else:
            a = a - 0.3
            left(3)
            forward(a)
    end_fill()

    # 鱼
    penup()
    setpos(-TREEX + 130, -window_height() / 2 + 45)
    pendown()
    fish()
    penup()
    setpos(-TREEX + 152, -window_height() / 2 + 120)
    pendown()
    fish()
    penup()
    setpos(-TREEX + 102, -window_height() / 2 + 90)
    pendown()
    fish()
    penup()
    setpos(-TREEX + 8, -window_height() / 2 + 110)
    pendown()
    fish()
    penup()
    setpos(-TREEX + 50, -window_height() / 2 + 40)
    pendown()
    fish()
    penup()
    setpos(-TREEX + 70, -window_height() / 2 + 130)
    pendown()
    fish()

    # 对话框
    penup()
    setpos(TREEX + TREEWIDTH // 2 + 30, -window_height() / 2 + 120)
    setheading(270)
    a = 0.4
    pendown()
    pencolor('blue')
    pensize(2)
    x = 0
    y = 0
    for i in range(1, 120):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.1
            left(3)
            forward(a)
        else:
            a = a - 0.1
            left(3)
            forward(a)
            if i == 100:
                x = xcor()
                y = ycor()
    penup()
    setpos(x, y)
    pendown()
    setheading(150)
    forward(15)
    setheading(300)
    forward(16)
    penup()
    setpos(x - 5, y - 25)
    pendown()
    pencolor('black')
    write('我的鱼在哪里？', align="left", font=("宋体", 8))

    # 标题
    penup()
    setpos(-100, window_height() / 2 - 100)
    write('缘木求鱼', align='left', font=('宋体', 35))
    done()

