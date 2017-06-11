
print('\n\n')
print('~~~~~~~~~~~排序算法~~~~~~~~~~~~~~~')

print(sorted([36, 5, -12, 9, -21]))#Python内置的sorted()函数就可以对list进行排序

print(sorted([36, 5, -12, 9, -21],key=abs))#sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))#现忽略大小写的排序

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]

def by():
	L2=sorted(L,key=by_name)
	return L2
print(by())

