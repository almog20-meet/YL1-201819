from turtle import *
import random
import turtle
import math

class Ball(Turtle):
	def __init__ (self, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10.0)
		self.radius = radius
		self.color(color)
		self.speed(speed)


ball1 = Ball(50, "red", 5)
ball2 = Ball(75, "blue", 5)
ball3 = Ball(90, "green", 5)
def check_collision(ball1, ball2):
 	ball1_x, ball1_y = ball1.pos()
	ball2_x, ball2_y = ball2.pos()
	

	D = math.sqrt(math.pow(ball1_x - ball2_x , 2) + math.pow(ball2_y - ball1_y, 2))

	if (ball1.radius + ball2.radius) >= D :
		print ("Collisions")

	else : 
		print ("Not Collisions")



balls_list= [ball1, ball2, ball3]
def check_collision2(balls_list):

	for i in range (len(balls_list)):
		list2= balls_list
		for j in range (len(list2)):
			if balls_list[i] != list2[j]:
				check_collision(balls_list[i], list2[j])
		else:
			print ("Not Collisions")

ball1.pu()
ball1.goto(100,100)

check_collision2(balls_list)
check_collision(ball1, ball2)
turtle.mainloop()

