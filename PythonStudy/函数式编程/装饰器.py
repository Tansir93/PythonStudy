print("/n/n")
print("~~~~~~~~~~~~~~~~~装饰器~~~~~~~~~~~~~~~")

def now():
    print('2015-3-25')

f = now
f()

print(now.__name__)#函数对象有一个__name__属性，可以拿到函数的名字
print(f.__name__)

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log#把@log放到now()函数的定义处，相当于执行了语句：now = log(now)
#调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志
def now():
    print('2015-3-25')

now()


def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2015-3-25')