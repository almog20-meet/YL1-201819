from turtle import *

class Ball(Turtle):
	def __init__(self, x, y, dx, dy, r, color):
		Turtle.__init__(self)
		self.pu()
		self.dx = dx
		self.dy = dy
		self.r = r
		self.x = x
		self.y = y
		self.color(color) 
		self.goto(x,y)
		self.shape("circle")
		self.shapesize(r/10)

	def move(self, screen_width, screen_height):
		current_x= self.pos()[0]
		new_x = current_x + self.dx 
		#y new x
		current_y= self.pos()[1]
		new_y = current_y + self.dy

		#ball side
		right_side = new_x + self.r
		left_side = new_x - self.r
		up_side= new_y + self.r
		down_side = new_y - self.r

		#go to new x and y
		self.goto(new_x, new_y)

		#checking edges
		#check right side
		if right_side > screen_width:
			self.dx = self.dx * (-1)
			#print("you hit the right side")

		#check left side
		if left_side < -screen_width:
			self.dx = self.dx * (-1)
			#print("you hit the left side")	

		#check up side
		if up_side > screen_height:
			self.dy = self.dy * (-1)
			#print("you hit the up side")

		#check down side
		if down_side < -screen_height:
			self.dy = self.dy * (-1)
			#print("you hit the down side")


	#new bballll
	def new_Ball(self, x, y, dx, dy, r, color):
		self.pu()
		self.dx = dx
		self.dy = dy
		self.r = r
		self.color(color) 
		self.goto(x,y)
		self.shape("circle")
		self.shapesize(r/10)
