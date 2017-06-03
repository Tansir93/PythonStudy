print("/n/n")
print("~~~~~~~~~~~~~~~~~循环~~~~~~~~~~~~~~~~~~")
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

print(list(range(5)))#range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)
