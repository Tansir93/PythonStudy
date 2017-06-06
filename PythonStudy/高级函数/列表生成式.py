print('\n\n')
print('~~~~~~~~~~~列表生成式~~~~~~~~~~~~~~~')

print(list(range(1, 11)))#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list([x * x for x in range(1, 11)]))#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print([x * x for x in range(1, 11) if x % 2 == 0])

print([m + n for m in 'ABC' for n in 'XYZ'])#['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

#和上面形式等效
for m in 'ABC':
	for n in 'XYZ':
		print(m+n)



#列出当前目录下的所有文件和目录名
import os # 导入os模块，模块的概念后面讲到
print([d for d in os.listdir('.')]) # os.listdir可以列出文件和目录

d = {'x': 'A', 'y': 'B', 'z': 'C' }#for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value
for k, v in d.items():
    print(k, '=', v)

L1 = ['Hello', 'World', 18, 'Apple', None]
print([n for n in L1 if isinstance(n,str)])
