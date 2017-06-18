print('/n/n')
print('~~~~~~~~~~~~~~继承和多态~~~~~~~~~~~~~')

class Animal(object):
	def run(self):
		print("Animal is runing..")

class Dog(Animal):

	def run(self):
	    print("Dog is runing...")
	pass

class Cat(Animal):
	def run(self):
	    print("Cat is runing...")
	pass

dog=Dog()
dog.run()

cat=Cat()
cat.run()

a = list() # a是list类型
b = Animal() # b是Animal类型
c = Dog() # c是Dog类型

#判断一个变量是否是某个类型可以用isinstance()判断
isinstance(a, list)
isinstance(b, Animal)
isinstance(c, Dog)

#c不仅仅是Dog，c还是Animal
isinstance(c, Animal)


def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())

run_twice(Dog())

run_twice(Cat())


print('/n/n')
print('~~~~~~~~~~~~~~静态语言 vs 动态语言~~~~~~~~~~~~~')
class Timer(object):
    def run():
        print('Start...')

run_twice(Timer)