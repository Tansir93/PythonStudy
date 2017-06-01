print("\n\n")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~字符串~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#字符串
print("\"hello\" world");#\转译符 \n表示换行，\t表示制表符，字符\本身也要转义
print(r"\\hello\\ world");#Python还允许用r''表示''内部的字符串默认不转义
print("hello\nworld");#\n换行
print('''hello
...world''');#用'''...'''的格式表示多行内容
print("\n\n")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~布尔值~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#布尔值
age=19;
if age >= 18:
    print('adult')
else:
    print('teenager')

print("\n\n")
print("~~~~~~~~~~~~~~~~~~~~~~~~~变量~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#变量
a=1;#int
print(a);
a="1";#string
print(a);
a=True;#bool
print(a);
print("\n\n")
print("~~~~~~~~~~~~~~~~~~~~~~~~~常量~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
A=12;
print(10/3)#输出:3.33333333333333333  浮点
print(10//3)#输出:3  整数
print(10%3)#输出:1
