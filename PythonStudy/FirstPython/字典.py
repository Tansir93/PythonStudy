print("/n/n")
print("~~~~~~~~~~~~~~~~~字典~~~~~~~~~~~~~~~~~~")
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}#创建一个dict
print(d['Michael'])

d['Adam'] = 67
print(d['Adam'])

print('Thomas' in d)#通过in判断key是否存在

print(d.get('Thomas'))#如果key不存在，可以返回None，或者自己指定的value
print(d.get('Thomas',-1))

d.pop('Bob')
print(d)

print("/n/n")
print("~~~~~~~~~~~~~~~~~set~~~~~~~~~~~~~~~~~~")
s = set([1, 2, 3])#创建一个set
print(s)#{1,2,3}
s = set([1, 1, 2, 2, 3, 3])#重复元素在set中被自动过滤
print(s)#{1,2,3}
s.add(4)#通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
print(s)#{1,2,3,4}
s.remove(4)#通过remove(key)方法可以删除元素
print(s)#{1,2,3}
#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1&s2)#交集{2,3}
print(s1|s2)#并集{1,2,3,4}



