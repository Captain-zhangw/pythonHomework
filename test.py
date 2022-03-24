from mypackage import painting

encodings = 'UTF-8'
translator = {'ā': 'a', 'á': 'a', 'ǎ': 'a', 'à': 'a',
              'ō': 'o', 'ó': 'o', 'ǒ': 'o', 'ò': 'o',
              'ē': 'e', 'é': 'e', 'ě': 'e', 'è': 'e',
              'ī': 'i', 'í': 'i', 'ǐ': 'i', 'ì': 'i',
              'ū': 'u', 'ú': 'u', 'ǔ': 'u', 'ù': 'u',
              'ǖ': 'v', 'ǘ': 'v', 'ǚ': 'v', 'ǜ': 'v'
              }


def translate(trans):
    temp = ''
    for i in trans:
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
        self.han = han
        self.pinyin = pinyin
        self.vis = False
        self.head = translate(pinyin[0])
        self.tail = translate(pinyin[-1])


chengyutxt = open('./chengyu.txt', 'r', encoding='UTF-8')
chengyulist = [i.split(' ==> ') for i in chengyutxt.readlines()]
Dragon = []
res = {}
vis = {}
for i in range(0, len(chengyulist)):
    Dragon.append(chengyu(chengyulist[i][0][1:len(chengyulist[i][0])], chengyulist[i][1][0:-1].split(' ')))
for i in Dragon:
    if i.head in res:
        res[i.head].append(i)
    else:
        res[i.head] = [i]
temp = res['fen']
paintlist = ['玉石俱焚']
for i in range(0, 9):
    for i in temp:
        if i.han not in vis:
            paintlist.append(i.han)
            temp = res[i.tail]
            vis[i.han] = True
            break
painting.paint()
painting.setpos(painting.window_width() / 2 - 100, painting.window_height() / 2 - 100)
j = 0
painting.color('black')

for i in paintlist:
    painting.goto(painting.window_width() / 2 - 100, painting.window_height() / 2 - 100 - j * 30)
    painting.write(i, align='left', font=('宋体', 15))
    j += 1
x = painting.xcor()
y = painting.ycor()
painting.done()
