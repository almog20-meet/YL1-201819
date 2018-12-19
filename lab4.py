"""
#problem 1
class Animal(object):
	def __init__(self, sound, name, age, fav_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.fav_color = fav_color
	def eat (self, food):
		print ("Yummy!!" + self. name + " is eating " + food)
	def description (self):
		print (self.name + " is " + self.age + " years old and love the color " + self. fav_color)

Cat = Animal("meow", "Mitzi", "4", "red")
Cat.eat("bonzo")
Cat.description()
"""

"""
#problem2: 

class Animal(object):
	def __init__(self, sound, name, age, fav_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.fav_color = fav_color
	def eat (self, food):
		print ("Yummy!!" + self. name + " is eating " + food)
	def description (self):
		print (self.name + " is " + self.age + " years old and love the color " + self. fav_color)
	def make_sound (self):
		for i in range (3):
			print(self.sound)

Cat = Animal("meow", "Mitzi", "4", "red")
Cat.eat("bonzo")
Cat.description()
Cat.make_sound()
"""

"""
#problem 3:
#part1
class Person():
	def __init__(self, name, age, city, gender, fav_clr, hair_clr, weight):
		self.name = name
		self.age = age
		self.city = city
		self.gender = gender
		self.fav_clr = fav_clr
		self.hair_clr = hair_clr
		self.weight = weight
	def Sport (self):
		self.weight -=10
	def BD(self):
		self.age +=1
		print ("happy Birtday" + self.name + " is " + self.age + " years old")
	#part 3
	def Eat (self):
		self.weight = self.weight + 5
		print (self.name + " just aet and now her weight is " + self.weight + )
#part 2
person1 = Person("Noya", "15" , "Tizinabe", "Other", "pink" , "brown" , "200")
person1.eat()

"""
"""
class Person():
	def __init__(self, name, age, city, gender, fav_clr, hair_clr, weight):
		self.name = name
		self.age = age
		self.city = city
		self.gender = gender
		self.fav_clr = fav_clr
		self.hair_clr = hair_clr
		self.weight = weight
	def Eat (self):
		self.weight = self.weight + 5
	def Sport (self):
		self.weight -=10
	def BD(self):
		self.age +=1
		print ("happy Birtday" + self.name + " is " + self.age + " years old")
#extra
class Song():
	def __init__(self, lyrics):
		self.lyrics = lyrics
	def Sing_me_a_song(self):
		for lyric in self.lyrics:
			print (lyric)


Person1 = Person("Batia", 24, "Hor", "girl", "red", "Blond", 74 )
Person1.Eat()
print (Person1.weight)
Person1.BD()
print (Person1.age)
for i in range (10):
	Person1.Sport()
	print (Person1.weight)

flower_song = Song([ "Roses are red" , "Violets are blue", "i wrote this poem for you"])
flower_song.Sing_me_a_song()
"""
