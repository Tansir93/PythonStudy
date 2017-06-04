print("/n/n")
print('~~~~~~~~~~~~~~~~~~位置参数~~~~~~~~~~~~~~~~~~~')
def power(x):#x就是位置参数
    return x * x

def power(x, n):#x和n，这两个参数都是位置参数，调用函数时，传入的两个值按照位置顺序依次赋给参数x和n。
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print("/n/n")
print('~~~~~~~~~~~~~~~~~~默认参数~~~~~~~~~~~~~~~~~~~')
def power(x, n):#把第二个参数n的默认值设定为2
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

def add_end(L=[]):
    L.append('END')
    return L
add_end()
add_end()
print(add_end())#['END','END','END']

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print("/n/n")
print('~~~~~~~~~~~~~~~~~~可变参数~~~~~~~~~~~~~~~~~~~')
def calc(*numbers):#定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(1, 2))
nums = [1, 2, 3]
print(calc(*nums))#Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去

print("/n/n")
print('~~~~~~~~~~~~~~~~~~关键字参数~~~~~~~~~~~~~~~~~~~')
def person(name, age, **kw):#函数person除了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数
    print('name:', name, 'age:', age, 'other:', kw)

print( person('Michael', 30))
person('Bob', 35, city='Beijing')#可以传入任意个数的关键字参数

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])#和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)#将上面简化后写法

print("/n/n")
print('~~~~~~~~~~~~~~~~~~命名关键字参数~~~~~~~~~~~~~~~~~~~')
def person(name, age, *, city, job):#和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
    print(name, age, city, job)

def person(name, age, *args, city, job):#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
    print(name, age, args, city, job)

person('Jack', 24, city='Beijing', job='Engineer')#命名关键字参数必须传入参数名
#如果缺少参数名city和job，Python解释器把这4个参数均视为位置参数，但person()函数仅接受2个位置参数。

def person(name, age, *, city='Beijing', job):#命名关键字参数可以有缺省值，从而简化调用
    print(name, age, city, job)

print("/n/n")
print('~~~~~~~~~~~~~~~~~~参数组合~~~~~~~~~~~~~~~~~~~')
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

#在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去。
print(f1(1, 2))
#a = 1 b = 2 c = 0 args = () kw = {}
print(f1(1, 2, c=3))
#a = 1 b = 2 c = 3 args = () kw = {}
print(f1(1, 2, 3, 'a', 'b'))
#a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
print(f1(1, 2, 3, 'a', 'b', x=99))
#a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
print(f2(1, 2, d=99, ext=None))
#a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}

#通过一个tuple和dict，你也可以调用上述函数
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
print(f1(*args, **kw))
#a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
print(f2(*args, **kw))
#a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}
