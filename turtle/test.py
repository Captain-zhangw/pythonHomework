from mypackage import painting

encodings = 'UTF-8'

# 将带音调的字母转换为不带音调的字母的字典表
translator = {'ā': 'a', 'á': 'a', 'ǎ': 'a', 'à': 'a',
              'ō': 'o', 'ó': 'o', 'ǒ': 'o', 'ò': 'o',
              'ē': 'e', 'é': 'e', 'ě': 'e', 'è': 'e',
              'ī': 'i', 'í': 'i', 'ǐ': 'i', 'ì': 'i',
              'ū': 'u', 'ú': 'u', 'ǔ': 'u', 'ù': 'u',
              'ǖ': 'v', 'ǘ': 'v', 'ǚ': 'v', 'ǜ': 'v'
              }


# 函数实现的功能为将带音调的字母转换为不带音调的字母
def translate(trans):
    temp = ''
    for i in trans:
        # 判断ascii码
        if (97 <= ord(i) <= 122) or (65 <= ord(i) <= 90):
            temp = temp + i
        else:
            try:
                temp = temp + translator[i]
            except KeyError:
                print('There is a KeyError!Maybe the chengyu.txt have illegal char')
    return temp


class chengyu:
    def __init__(self, han, pinyin):
        # 存储的是汉字
        self.han = han
        # 存储的是拼音
        self.pinyin = pinyin
        # 存储的是第一个字的拼音
        self.head = translate(pinyin[0])
        # 存储的是最后一个字的拼音
        self.tail = translate(pinyin[-1])


chengyutxt = open('./chengyu.txt', 'r', encoding='UTF-8')
chengyulist = [i.split(' ==> ') for i in chengyutxt.readlines()]
Dragon = []
res = {}
vis = {}
for i in range(0, len(chengyulist)):
    # 将成语按照汉字和拼音存入类中
    Dragon.append(chengyu(chengyulist[i][0][1:len(chengyulist[i][0])], chengyulist[i][1][0:-1].split(' ')))
for i in Dragon:
    # 将头拼音相同的成语保存到同一个字典里
    if i.head in res:
        res[i.head].append(i)
    else:
        res[i.head] = [i]
temp = res['shan']
paintlist = ['缘木求鱼', '与人为善']
for i in range(1, 10):
    # 以下为判断此成语是否使用过
    for j in temp:
        if j.han not in vis and j.han[0] != paintlist[i][-1]:
            paintlist.append(j.han)
            temp = res[j.tail]
            vis[j.han] = True
            break
painting.paint()
painting.setpos(painting.window_width() / 2 - 100, painting.window_height() / 2 - 100)
j = 0
painting.color('black')
# 以下开始在画布上接龙成语
for i in paintlist:
    painting.goto(painting.window_width() / 2 - 100, painting.window_height() / 2 - 30 - j * 30)
    painting.write(i, align='left', font=('宋体', 15))
    j += 1
x = painting.xcor()
y = painting.ycor()
painting.goto(x, y - 30)
painting.write('接龙完成', align='left', font=('宋体', 15))
y = y - 50
# 以下开始写学号姓名和班级
painting.goto(x, y - 60)
painting.write('Captainzw', align='left', font=('宋体', 15))
painting.goto(x, y - 90)
painting.write('计20x', align='left', font=('宋体', 15))
painting.goto(x, y - 120)
painting.write('42024xxx', align='left', font=('宋体', 15))
# 以下绘制条形码
x = painting.xcor() - 70
y = painting.ycor() - 15

txmwidth = 50

numberlist = ['110100111', '0010110111', '0001100110011011', '00010100011101110110110111010001100011101011']
painting.setheading(270)
painting.pensize(2)
count = 2
count2 = 0
for i in numberlist:
    for j in range(0, len(i)):
        if i[j] == '1':
            painting.penup()
            painting.goto(x + count, y)
            painting.pendown()
            painting.forward(txmwidth)
        count += 2
    count2 += 1
painting.penup()
painting.goto(x + 50, y - txmwidth - 25)
painting.pendown()
painting.write("42024xxx", align='left', font=('宋体', 15))
painting.done()
