print('\n\n')
print('~~~~~~~~~~~切片~~~~~~~~~~~~~~~')

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print( L[0:3])#取前3个元素
print( L[:3])#如果第一个索引是0，还可以省略
print(L[1:3])#以从索引1开始，取出2个元素出来
print(L[-2:])#倒数切片
print(L[-2:-1])
L = list(range(100))
print( L[:10:2])#前10个数，每两个取一个
print(L[::5])#所有数，每5个取一个
print(L[:])#原样复制一个list
print((0, 1, 2, 3, 4, 5)[:3])#tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作
print('ABCDEFG'[:3])#字符串也可以看成是一种list，每个元素就是一个字符。

print('\n\n')
print('~~~~~~~~~~~迭代~~~~~~~~~~~~~~~')
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:#dict迭代,dict迭代的是key
    print(key)#因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。

for ch in 'ABC':#字符串也是可迭代对象，因此，也可以作用于for循环
    print(ch)

from collections import Iterable#通过collections模块的Iterable类型判断一个对象是可迭代对象
isinstance('abc', Iterable) # str是否可迭代

for i, value in enumerate(['A', 'B', 'C']):#Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
    print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:#for循环里，同时引用了两个变量
   print(x, y)