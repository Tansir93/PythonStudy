print("/n/n")
print("~~~~~~~~~~~~~~~~~list~~~~~~~~~~~~~~~~~~")
classmates = ['Michael', 'Bob', 'Tracy']#list是一种有序的集合
print(classmates)
print(len(classmates))#获取list元素个数
print(classmates[0])
print(classmates[-1])#取最后一个元素
classmates.append('Adam')#追加元素到末尾
print(classmates)
classmates.insert(1,"jack")#插入指定位置
print(classmates)
classmates.pop(1)#删除指定位置元素
print(classmates)
classmates[1]='sarah'#赋值
print(classmates)

classmates=[123,'apple',True]#允许不同数据类型
print(classmates)

classmates=[123,'apple',[123,'pop'],True]#list元素也可以是另一个list
print(classmates)

print(classmates[2][1])#获取嵌套list中元素


print("/n/n")
print("~~~~~~~~~~~~~~~~~tuple~~~~~~~~~~~~~~~~~~")
classmates = ('Michael', 'Bob', 'Tracy')#classmates这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，tuple使用(),list使用[]。
t=(1,2)
print(t)#(1,2)
t=()#定义空tuple
print(t)#()
t=(1)#括号()既可以表示tuple，又可以表示数学公式中的小括号
print(t)#1
t=(1,)#只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
print(t)#(1,)
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)