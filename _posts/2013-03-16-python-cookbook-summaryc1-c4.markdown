---
date: 2013-03-16 02:02:58+00:00
layout: post
title: Python Cookbook Summary(C1-C4)
categories:
- Python
description: "记录下来，作为总结。"
---

不一定全是书中讲授的内容，也有部分是书中涉及到但是没有系统讲述的。记录下来，作为总结。





## 第一章：文本





### 字符与字符值的转换







  * ord('a')


  * chr(97)


  * int('10111011', 2)





### strip()





方法定义：`strip([chars])`。返回一个在两端删除参数字符的原字符串的拷贝。如果没有参数，会删除空格。  
除此以外，还有lstrip()和rstrip()，分别作用在开头和结尾。





### translate方法的使用





先看定义：`s.translate(table[, deletechars])`  
效果就是对字符串s移除deletechars包含的字符，然后剩下的字符按照table的映射关系进行映射。而table就是用maketrans方法生成的。  
再看maketrans.用法是`string.maketrans(input, output)`，input和output长度要一样。  
看个例子：




    
    import string
    s= 'abcdefg-1234567'
    table = string.maketrans('abc', 'ABC')
    s.translate(table, 'ab12')
    #output:'Cdef-34567'





如何把要保留的字符变成要删除的字符：




    
    allchars = string.maketrans('', '')
    delchars = allchars.translate(allchars, keep)



## 第二章：文件





### 读取和写入





python支持对文件对象的迭代处理




    
    for line in input:
        process(line)




如果不确定文件会用什么样的换行符，或者不确定所在的操作系统，可以将open函数的第二个参数设置为'rU'，表示通用换行符。  
[文件对象的方法](http://docs.python.org/2/tutorial/inputoutput.html#methods-of-file-objects)：







  * `f.read(size)` 当不给出size时，会读取整个文件内容。当文件指针指向文件最后时，会返回空字符串''。


  * `f.readline()` 将读取一整行，直到遇到换行符'\n'。


  * `f.readlines()` 将返回一个包含所有行的**列表**。


  * `f.write(string)` 将string写入文件。


  * `f.tell()` 返回一个整数，表示文件对象在文件中的当前位置。


  * `f.seek(offset[, from_what])` 重新定位文件对象位置，from_what的值表示从哪里开始算起。0（默认）：从文件头；1：从当前位置；2：从文件尾。





### sys.argv[]





sys.argv是用来获取命令行参数的，它是一个列表。sys.argv[0]是当前文件名，参数从sys.argv[1](http://docs.python.org/2/tutorial/inputoutput.html#methods-of-file-objects)开始。  
有一道题目，要求打印当前程序的代码。使用sys.argv即可实行。




    
    import sys
    print open(sys.argv[0], 'r').read()





### enumerate的用法





计算大文件的行数时用到了enumerate：




    
    count = -1
    for count, line in enumerate(open(thefilepath, 'rU')):
        pass
    count += 1





先看看enumerate的定义：




    
    def enumerate(sequence, start=0):
        n = start
        for elem in sequence:
            yield n, elem
            n += 1





它是一个生成器，返回索引和索引内容。看个例子：




    
    mylist = ["a","b","c","d"]
    for i, j in enumerate(mylist):
        print i, j
    
    output:
    0 a
    1 b
    2 c
    3 d





### os.walk()





os.walk()是标准库模块os中的生成器，它返回一个三元的tuple(dirpath, dirnames, filenames),分别表示起始路径，文件夹名和文件名。  
方法定义：`os.walk(top, topdown=True, onerror=None, followlinks=False)`





## 第三章 时间和财务计算





### [datetime模块](http://docs.python.org/2/library/datetime.html#available-types)





包含几个类：







  * datetime.date


  * datetime.time


  * datetime.datetime


  * datetime.datedelta


  * datetime.tzinfo





### [datedelta对象](http://docs.python.org/2/library/datetime.html#timedelta-objects)





定义：class datetime.timedelta([days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]]) All arguments are optional and default to 0. Arguments may be ints, longs, or floats, and may be positive or negative.





有如下转换：







  * A millisecond is converted to 1000 microseconds.


  * A minute is converted to 60 seconds.


  * An hour is converted to 3600 seconds.


  * A week is converted to 7 days.





所以必须满足：







  * 0 <= microseconds < 1000000


  * 0 <= seconds < 3600*24


  * -999999999 <= days <= 999999999





### datetime.date对象





一个很重要的方法就是today()




    
    import datetime
    print datetime.date.today()
    #output:datetime.date(2013, 3, 11)





操作：







  * date2 = date1 + timedelta 


  * date2 = date1 - timedelta 


  * timedelta = date1 - date2


  * date1 < date2





### datetime.datetime对象





它也有一个方法：today()。但是相比date，它的today方法还会输出具体时间(time)。




    
    print datetime.datetime.today()
    #output: datetime.datetime(2013, 3, 11, 15, 14, 37, 452605)





## 第四章 Python技巧





### [字典dict](http://docs.python.org/2/library/stdtypes.html#mapping-types-dict)





定义字典方法如下：




    
    a = dict(one=1, two=2, three=3)
    b = {'one': 1, 'two': 2, 'three': 3}
    c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
    d = dict([('two', 2), ('one', 1), ('three', 3)])
    e = dict({'three': 3, 'one': 1, 'two': 2})
    a == b == c == d == e
    #output:True





字典具有的一些方法：







  * len(d)


  * d[key]


  * d[kye] = value


  * del d[key]


  * key (not)in d


  * iter(d):Return an iterator over the keys of the dictionary. 


  * get(key[,default]):如果key存在，返回d[key]，否则返回default.如果default为None,则引发KeyError.


  * has_key(key)


  * items()/iteritems():返回包含(key, value)的列表。


  * pop(key[,default]):类似于get(),只是返回后删除掉d[key].





### copy和deepcopy的区别





The difference between shallow and deep copying is only relevant for compound objects.简单来说，就是copy是浅拷贝，只会整个复合对象，其子对象仍然使用引用。




    
    import copy
    a = [1,2,3,[4,5,6,[7,8,9]]]
    b = copy.copy(a)
    print a
    [1, 2, 3, [4, 5, 6, [7, 8, 9]]]
    print b
    [1, 2, 3, [4, 5, 6, [7, 8, 9]]]
    b[0] = 10
    print b
    [10, 2, 3, [4, 5, 6, [7, 8, 9]]]
    print a
    [1, 2, 3, [4, 5, 6, [7, 8, 9]]]  # a没有变化
    b[3][0] = 11
    print b
    [10, 2, 3, [11, 5, 6, [7, 8, 9]]]
    print a
    [1, 2, 3, [11, 5, 6, [7, 8, 9]]]  # a有变化





上述例子中，b[0]不是复合对象，所以a[0]不会改变。但是b[3][0]仍然指向a[3][0]，所以会改变。





### isinstance()





是一个判断对象类型的函数。  
isinstance(object, class-or-type-or-tuple) -> bool,即其第一个参数为对象，第二个为类型名或类型名的一个列表。其返回值为布尔型。





### *args和**kwds语法





它们是用来传递参数的，星号后面跟的都是标识符，可以是任意的。  

两者有何不同，看看例子就会明白：
example-1:




    
    def test_var_args(farg, *args):
        print "formal arg:", farg
        for arg in args:
            print "another arg:", arg
    test_var_args(1, "two", 3)
    #output:
    formal arg: 1
    another arg: two
    another arg: 3





example-2:




    
    def test_var_kwargs(farg, **kwargs):
    print "formal arg:", farg
    for key in kwargs:
        print "another keyword arg: %s: %s" % (key, kwargs[key])
    test_var_kwargs(farg=1, myarg2="two", myarg3=3)
    #output:
    formal arg: 1
    another keyword arg: myarg2: two
    another keyword arg: myarg3: 3



