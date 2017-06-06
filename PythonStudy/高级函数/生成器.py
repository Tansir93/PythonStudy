print('\n\n')
print('~~~~~~~~~~~生成器~~~~~~~~~~~~~~~')
print([x * x for x in range(10)])#list
g=(x * x for x in range(10))#generator
#在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
print(next(g))#通过next获取下一个元素
print(next(g))
print(next(g))
for n in g:#for从next后面开始迭代，
	print(n)

def fib(max):#斐波拉契数列
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b#一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
        a, b = b, a + b
        n = n + 1
    return 'done'
