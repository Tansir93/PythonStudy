print("\n\n")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~字符串编码~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(ord("A"))#ord()函数获取字符的整数表示
print(chr(66))#chr()函数把编码转换为对应的字符
print('\u4e2d\u6587')#字符的整数编码用十六进制
print('ABC'.encode('ascii'))#纯英文的str可以用ASCII编码为bytes
print( '中文'.encode('utf-8'))#纯英文的str可以用ASCII编码为bytes
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print(len('ABC'))#计算str包含多少个字符

print("\n\n")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~格式化~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print('Hello, %s' % 'world')#%运算符就是用来格式化字符串的。
print('Hi, %s, you have $%d.' % ('Michael', 1000000))#如果只有一个%?，括号可以省略。
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
print('Age: %s. Gender: %s' % (25, True))
print('growth rate: %d %%' % 7)
