print('/n/n')
print('~~~~~~~~~~~~~~面向对象编程~~~~~~~~~~~~~')

class Student(object):

    def __init__(self, name, score):#通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去,__init__方法的第一个参数永远是self，表示创建的实例本身
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()


print('/n/n')
print('~~~~~~~~~~~~~~类和实例~~~~~~~~~~~~~')
class Student(object):#class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的
    pass

bart = Student()#创建实例
bart.name = 'Bart Simpson'#可以自由地给一个实例变量绑定属性
print(bart.name)