

# #problem 1:
# from turtle import *
# import turtle 
# import random
# colormode(255)
# class Square (Turtle):
# 	def __init__ (self,size):
# 		Turtle.__init__(self)
# 		self.shape("square")
# 		self.size = size
# 		self.shapesize(size*size)
# 	def random_color(self):
# 		r = random.randint(0,255)
# 		b = random.randint(0,255)
# 		g = random.randint(0,255)
# 		self.color(r, g, b)

# square1= Square(5)
# square1.random_color()

# turtle.mainloop()



# #extra
# class Rectangle(object):
# 	def __init__ (self, width, height):
# 		self.width = width
# 		self.height = height
# 	def Area (self):
# 		area= self.width * self.height
# 		print (area)
# 	def Perimeter (self):
# 		perimeter =(self.width + self.height)*2
# 		print (perimeter)
# 	def Print_Properties(self):
# 		print ("the width is " + str(self.width) + " and the height is " + str(self.height))

# shape1 = Rectangle(5,6)
# shape1.Area()
# shape1.Perimeter()
# shape1.Print_Properties()


#problem2
from turtle import *
import turtle 
import random
colormode(255)
class Hexagon (Turtle):
	def __init__ (self, size):
		Turtle.__init__(self)
		self.size=size
		self.shapesize(size*size)
		begin_poly()
		for i in range (6):
			self.fd(100)
			self.right(60)
		end_poly()
		p = get_poly()
		register_shape("Hexagon", p)
		self.shape("Hexagon")

	def speed (self):
		turtle.speed(5)

hexagon1=Hexagon(2)
hexagon1.speed()
turtle.mainloop()