print('/n/n')
print('~~~~~~~~~~~~~~获取对象~~~~~~~~~~~~~')

print(type(123))

print(type(abs))

a=abs
print(type(a))

import types
def fn():
	pass

#判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量
print(type(fn)==types.FunctionType)

print('/n/n')
print('~~~~~~~~~~~~~~使用isinstance()~~~~~~~~~~~~~')

class Animal(object):
	def run(self):
		print("Animal is runing..")

class Dog(Animal):

	def run(self):
	    print("Dog is runing...")
	pass

class Cat(Animal):
	def run(self):
	    print("Cat is runing...")
	pass

a=Animal()
d=Dog()
c=Cat()

print(isinstance(d,Dog))#T
print(isinstance(d,Animal))#T
print(isinstance(a,Dog))#F
print(type(d)==type(a))#F

#判断一个变量是否是某些类型中的一种
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

print('/n/n')
print('~~~~~~~~~~~~~~使用dir()~~~~~~~~~~~~~')
print(dir('ABC'))
#['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

class MyDog(object):
     def __len__(self):
         return 100
dog = MyDog()
print(len(dog))

class MyObject(object):
     def __init__(self):
         self.x = 9
     def power(self):
         return self.x * self.x

obj = MyObject()

print(hasattr(obj, 'x'))#存在属性X

print(hasattr(obj, 'y'))#F
print(setattr(obj, 'y', 19))#设置属性y
print(hasattr(obj, 'y'))#T

print(getattr(obj,'y'))#获取属性y

print(getattr(obj, 'z', 404)) # 获取属性'z'，如果不存在，返回默认值404

hasattr(obj, 'power') # 有属性'power'吗？
getattr(obj, 'power') # 获取属性'power'
fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
print(fn()) # 调用fn()与调用obj.power()是一样的