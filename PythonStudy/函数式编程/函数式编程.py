print("/n/n")
print("~~~~~~~~~~~~~~~~~变量可以指向函数~~~~~~~~~~~~~~~")
print( abs(-10))
print(abs)
a=abs#将abs函数赋值给一个变量
print(a)#变量可以指向函数
print(a(-1))

print("/n/n")
print("~~~~~~~~~~~~~~~~~函数名也是变量~~~~~~~~~~~~~~~")
#abs = 10#把abs指向10后，就无法通过abs(-10)调用该函数了！因为abs这个变量已经不指向求绝对值函数而是指向一个整数10！
#abs(-10)#由于abs函数实际上是定义在import builtins模块中的，所以要让修改abs变量的指向在其它模块也生效，要用import builtins; builtins.abs = 10。
print("/n/n")
print("~~~~~~~~~~~~~~~~~传入函数~~~~~~~~~~~~~~~")
def add(x, y, f):
    return f(x) + f(y)
print(add(-5, 6, abs))