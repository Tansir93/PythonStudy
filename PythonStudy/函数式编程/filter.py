print("/n/n")
print("~~~~~~~~~~~~~~~~filter~~~~~~~~~~~~~~~~~")
def is_odd(n):
    return lambda x: x % n == 1
print(list(filter(is_odd(2), [1, 2, 4, 5, 6, 9, 10, 15])))

#计算素数的一个方法是埃氏筛法
#构造一个从3开始的奇数序列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
#定义一个筛选函数
def _not_divisible(n):
    return  lambda x: x % n > 0#n之前迭代的n，x为通过it传入


def _not1(x):
	return x%n>0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

for n in primes():
    if n < 1000:
        print(n)
    else:
        break

print([1,2,3,2,1][::-1])