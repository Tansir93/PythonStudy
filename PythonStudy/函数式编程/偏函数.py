print("/n/n")
print("~~~~~~~~~~~~~~~~~偏函数~~~~~~~~~~~~~~~")
print(int('11',2))#int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换

def int2(x, base=2):#定义一个int2()的函数，默认把base=2传进去
    return int(x, base)

#functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2
import functools
int2 = functools.partial(int, base=2)#functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
print(int2('1000000'))

print(int2('1000000',base=10))#新的int2函数，仅仅是把base参数重新设定默认值为2，但也可以在函数调用时传入其他值

