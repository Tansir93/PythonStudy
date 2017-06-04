print("/n/n")
print("~~~~~~~~~~~~~~~调用函数~~~~~~~~~~~~~~~~~~~~~")
print(help(abs))#帮助函数
print(abs(-100))#绝对值
print(max(1,4,2))#返回最大值

print("/n/n")
print("~~~~~~~~~~~~~~~数据类型转换~~~~~~~~~~~~~~~~~~~~~")
print(int('123'))
print(float('12.12'))
print(str(123))
print(bool(1))

a=abs
print(a(-4))#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”

n1 = 255
print(hex(n1))

print("/n/n")
print("~~~~~~~~~~~~~~~定义函数~~~~~~~~~~~~~~~~~~~~~")
def my_abs(x):#函数名
    if x >= 0:
        return x#返回值
    else:
        return -x

print(my_abs(-3))

print("/n/n")
print("~~~~~~~~~~~~~~~空函数~~~~~~~~~~~~~~~~~~~~~")
def nop():
    pass
age=17
if age >= 18:#充当占位符，如果去掉pass程序将报错
    pass

print("/n/n")
print("~~~~~~~~~~~~~~~参数检查~~~~~~~~~~~~~~~~~~~~~")
def my_abs(x):
    if not isinstance(x, (int, float)):#对传入参数进行检查
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print("/n/n")
print("~~~~~~~~~~~~~~~返回多个值~~~~~~~~~~~~~~~~~~~~~")
import math#import math语句表示导入math包，并允许后续代码引用math包里的sin、cos等函数。

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

r = move(100, 100, 60, math.pi / 6)
print(r)#实际上，返回值是一个tuple
