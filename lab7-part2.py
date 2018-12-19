
# #problem 6
# class Bear():
# 	def __init__(self, name):
# 		self.name = name
# 		print("A new bear created. Its name is: " + self.name)
	
# 	def say_hi(self, name):
# 		self.name = name
# 		print("Hi! Im a bear. My name is " + self.name)
# my_bear = Bear("Danny")
# print(my_bear.say_hi("Bar"))


"""
 #problem 7
balloons = "5"
name = "Ron"
color = "Yellow"
print("This is a tale about" +" " + balloons + " " + "balloons. The first kid is " + " " + name + " " + "who got a" + " " + color + " " + "balloon")
"""

"""
 #problem 8
class Cake():
	def __init__ (self, flavor):
		self.flavor = flavor

	def eat (self):
		print("Yummy!!! Eating a" + " " +  self.flavor + " cake" )

cake = Cake("chocolate")
cake.eat()
# what I want to be printed: Yummy!!! Eating a chocolate cake :)
"""

#problem 9 
import math
class Cat():
	def __init__(self, name, age ):
		self.name = name
		self.age = 0
	def birthday(self):
		self.age += 1
		if self.age >= 100 :
			print("Dong dong, the cat is dead!")
		else:
			print(self.name + " hasing its " + str(self.age) + " birthday!")

my_cat = Cat("Mitzi", 8)
my_cat.birthday()
# what I want: my cat to  celebrate its 8th birthday (and all the 
# birthdays that come before that)