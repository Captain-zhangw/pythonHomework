# 表格上的皇后开发日记

---

## 开发流程

### 一、解决N皇后问题

N皇后问题是一道经典的算法题，利用了回溯递归的方法

具体思想是，从第一行开始遍历1-N列，要保证每行每列和两个对角线均不存在皇后，利用三个数组column,diag(i-j相同的关系),diag2(i+j相同的关系)标记是否曾经被访问过

如果找到了每行每列和两个对角线均不存在皇后，则递归进入下一行，继续上面的操作，如果遍历了每一列后都无法找到，就return返回，并把标记过的数组恢复

最后将结果存储在数组中

### 二、将N皇后结果输入到excel表格中

利用`openpyxl`库完成输入操作，创建新.xlsx格式的文件，并且获取工作页进行输入。

将表格渲染成黑白相间，可以利用判断(i+j)是否为偶数来判断填充黑色或是白色，背景为白色则字体为黑色，反之亦然

遍历存储数组中的所有结果，根据索引将结果输出到表格中

设置行高和列宽，字体的大小，水平居中和垂直居中，即完成了输入

---



## 效果截图

![image-20220331165058781](F:\学习\Python程序设计\code\image.png)

---

## 源代码

```python
import openpyxl as op
from openpyxl.styles import PatternFill
from openpyxl.styles import Alignment
from openpyxl.styles import Font
from openpyxl.utils import get_column_letter

n = int(input("请输入皇后个数:(建议输入数值在11及以下)\n"))

# 递归解决N皇后问题并且把分布结果存储在res数组中
column = [False] * (n + 1)
diag = [False] * 2 * (n + 1)
diag2 = [False] * 2 * (n + 1)
res = []
pres = [0] * (n + 1)


def function(n, k):
    if k == n + 1:
        res.append(pres.copy())
        return
    for i in range(1, n + 1):
        if column[i] is False and diag[k - i + n] is False and diag2[i + k] is False:
            column[i] = True
            diag[k - i + n] = True
            diag2[i + k] = True
            pres[k] = i
            function(n, k + 1)
            column[i] = False
            diag[k - i + n] = False
            diag2[i + k] = False
    return


# 开始操作excel表格
rowHeight = 32  # 行高
columnWidth = 8  # 列宽
function(n, 1)
wb1 = op.Workbook()
ws = wb1.active
for k in range(0, len(res) - 1, 2):
    for i in range(0, n):
        for j in range(1, n + 1):
            tempCell = ws.cell(i + 1 + k * 6, j)
            tempCell2 = ws.cell(i + 1 + k * 6, j + 12)
            tempCell.font = Font(color="111111", size='25')
            tempCell2.font = Font(color="111111", size='25')
            if (i + j) % 2 == 0:
                tempCell.fill = PatternFill(fill_type='solid', start_color='111111')
                tempCell.font = Font(color="ffffff", size='25')
                tempCell2.fill = PatternFill(fill_type='solid', start_color='111111')
                tempCell2.font = Font(color="ffffff", size='25')
            if res[k][i + 1] == j:
                tempCell.alignment = Alignment(horizontal="center", vertical='center')
                tempCell.value = '\u2655'
            if res[k + 1][i + 1] == j:
                tempCell2.alignment = Alignment(horizontal="center", vertical='center')
                tempCell2.value = '\u2655'
# 设置行高列宽
for i in range(1, ws.max_row + 1):
    ws.row_dimensions[i].height = rowHeight
for i in range(1, ws.max_column + 1):
    ws.column_dimensions[get_column_letter(i)].width = columnWidth
wb1.save("./fill.xlsx")
print("输出完成")

```

