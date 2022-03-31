# 成语接龙开发日记

---



## 开发流程

### 前期准备——将turtle绘图打包成第三方库

在进行成语接龙前要做的是先要将我的turtle绘图打包为第三方库可以供我调用。

因此我将我的所有绘图代码放进一个paint函数中，接下来开始打包

1. 我创建了一个`mypackage`文件夹，其中包含两个`py`文件，一个是`__init__.py`,另一个是`painting.py`。

2. 然后我在`mypackage`同级下建立了`setup.py`文件其中主要包括

   ```python
   from setuptools import setup,find_packages
   setup{
   	name='mypackage',
   	version='1.0',
   	package=find_packages()
   }
   ```

3. 执行`python setup.py bdist_egg`后可以生成几个文件

4. 到需要的文件夹下执行`python setup.py install`生成egg文件

5. 解压到python的`site-packages`文件夹下即可

6. 在新的`py`文件下`from mypackage import painting`成功导入

---



### Version  1.0——成语存储

观察`chengyu.txt`结构发现成语的存储结构为：

​	成语中文 ==> 成语拼音

那么就可以通过split()函数把成语分为两节，一节是中文成语，另一节是成语拼音

则将此两个存储进`chengyu`类里，由于不考虑音调的原因，用`translate()`函数把成语拼音改为不带音调的拼音

再在`chengyu`类中存入第一个字的拼音和最后一个字的拼音以用作可以后面的结论

---



### Version 2.0——成语分类

目标是用作成语接龙，则成语的分类就要用拼音来分类，而分类所需的是成语的首拼音，因为从上一个成语接龙时需要得知下一个成语的首拼音，因此利用上面成语存储后的结果用字典结构来分类成语

```python
translator = {'ā': 'a', 'á': 'a', 'ǎ': 'a', 'à': 'a',
              'ō': 'o', 'ó': 'o', 'ǒ': 'o', 'ò': 'o',
              'ē': 'e', 'é': 'e', 'ě': 'e', 'è': 'e',
              'ī': 'i', 'í': 'i', 'ǐ': 'i', 'ì': 'i',
              'ū': 'u', 'ú': 'u', 'ǔ': 'u', 'ù': 'u',
              'ǖ': 'v', 'ǘ': 'v', 'ǚ': 'v', 'ǜ': 'v'
              }
```

---



### Version 3.0——完成成语接龙并打印在画布上

 上面的成语存储和分类都完成了，那么只要开始遍历已存储的结构就可以了

先找到需要接龙的成语，取得他的尾部拼音，根据尾部拼音，通过字典结构找到此尾部拼音存储的成语，从中进行遍历选择合适的成语记录下来，再重复上述过程。共存储十个成语

此时开始调用第三方库的`paint()`函数将”缘木求鱼”，并选择合适位置将储存下来的接龙成语进行打印

---

### Version 4.0——名字班级学号条形码

此处较为简单，即在画布上打印名字学号和条形码

---

### Version 5.0——修复以上BUG

注意到成语接龙的字并不能相同，因此需要在接龙时判断成语的字并不能相同、

条形码无效，根据查阅资料，更改了条形码的结构，使得条形码可以扫出学号

---

### Version 5.1——小调整

进行了一些布局的小调整，满足题目其余的要求

---

## 其余问题

在进行成语接龙时还遇到了一些其他问题

例如：

- 接龙时发现`chengyu.txt`并不规范，有许多成语的拼音并不是拼音，可能被？代替了，这样会导致利用`translate（）`函数进行转换是发生错误。我的解决方法是将`translate()`函数放入

  ```python
  try:
  
  except KeyError:
  	print('There is a KeyError!Maybe the chengyu.txt have illegal char')
  ```

  这样出现错误时会打印字符串而不是终止程序

- 其实`.isalpha()`函数也会认为带音调的拼音为True，因此无法通过此方法分辨是否带音调，因此选用ASCII法来判断是否为英文字母

- 成语库中会出现很多成语没有的情况，导致接龙不到10个就结束了，暂时没有什么好方法，只能自己添加或者更换成语

- 成语库中并不是一个成语只出现一次，一个成语可能出现两次甚至三次（不清楚是否会更多），这就需要再利用一个字典存储那些成语被输出过了，保证接龙得到时候不会重复出现成语

---



## 程序效果截图

![image-20220327214900829](F:\学习\Python程序设计\第二次作业——成语接龙\image\image-20220327214900829.png)
