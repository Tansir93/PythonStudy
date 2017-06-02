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