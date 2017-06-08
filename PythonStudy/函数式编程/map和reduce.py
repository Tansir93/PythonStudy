print("/n/n")
print("~~~~~~~~~~~~~~~~map/reduce~~~~~~~~~~~~~~~~~")
def f(x):
     return x * x
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])#r中并不是map返回的结果，r只是赋值
print(list(r))#map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))#转成string


#reduce
from functools import reduce
def add(x, y):
    return x + y
print(reduce(add, [1, 3, 5, 7, 9]))#求和


def fn(x, y):
    return x * 10 + y
def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
print(reduce(fn, map(char2num, '13579')))#把str转换为int

#整理成函数
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))

#用lambda函数

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def big(s1):
	return s1[0:1].upper()+s1[1:].lower()
print(list(map(big,['adam', 'LISA', 'barT'])))

#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
	return reduce(lambda x,y:x*y,L)
print(prod([1,2,3,4]))


#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2float(s):
	x,y=s.split('.')
	return reduce(lambda x,y:x*10+y,map(char2num,x))+reduce(lambda x,y:x*10+y,map(char2num,y))/10**len(y);
print(str2float('123.456'))