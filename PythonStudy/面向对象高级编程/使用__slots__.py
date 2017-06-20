print('/n/n')
print('~~~~~~~~~~~~~~~~~使用__slots__~~~~~~~~~~~~')
class Student(object):
	def score(self,age):
		self.age=age


s=Student()
s.score=15
print(s.score)
s.name='Michael';#绑定一个属性
print(s.name);

def set_age(self,age):#定义一个函数作为实例方法
	self.age=age;

from types import MethodType
s.set_age=MethodType(set_age,s)#给实例绑定一个方法
s.set_age(25)#调用实例方法
print(s.age)

S2=Student()#创建新实例
#s2.set_age(25)#调用方法，无法调用。给一个实例绑定的方法，对另一个实例不起作用

#为了给所有实例都绑定方法，可以给class绑定方法
def set_score(self, score):
    self.score = score

Student.set_score=set_score
S2.set_score(100)
print(S2.score)


print('/n/n')
print('~~~~~~~~~~~~~~~~~使用__slots__~~~~~~~~~~~~')
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

s=Student()#创建新实例
s.name='Micheel'#绑定属性'name'
s.age=25
s.score=99#AttributeError: 'Student' object has no attribute 'score'

#使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class GraduateStudent(Student):
	pass
g = GraduateStudent()
g.score = 9999