print("/n/n")
print("~~~~~~~~~~~~~~~条件判断~~~~~~~~~~~~~~~~~~~")
age = 20
if age >= 18:#根据Python的缩进规则，如果if语句判断是True，就把缩进的两行print语句执行了
    print('your age is', age)
    print('adult')

age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')

age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

print("/n/n")
print("~~~~~~~~~~~~~~~input~~~~~~~~~~~~~~~~~~~")
birth = input('birth: ')#input()返回的数据类型是str
birth=int(birth)#int()把str转换成整数
if birth < 2000:
    print('00前')
else:
    print('00后')