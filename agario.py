import turtle
import time
import random
import math
from ball import Ball
import tkinter as tk
turtle.tracer(0)
turtle.hideturtle()
running = True
screen_width = turtle.getcanvas().winfo_width()/2
screen_height = turtle.getcanvas().winfo_height()/2

#create button
button = turtle.clone()
turtle.register_shape("replay.gif")
button.shape("replay.gif")
button.pu()
button.goto(0, 0)
#part 1 creating ball 
y_name = turtle.textinput("Input", "What is your name?")

my_ball= Ball(0,0 ,10,10, 20, "red")

#variables

number_of_balls= int(turtle.textinput("Input", "Choose your level"))
minimum_ball_radius = 5
maximum_ball_radius = 70
minimum_ball_dx = 5
maximum_ball_dx = 5.
minimum_ball_dy = -5.
maximum_ball_dy = 5.

#balls list
BALLS = []

#random ball
for i in range (number_of_balls):
	x = random.randint( -screen_width + maximum_ball_radius, screen_width - maximum_ball_radius)
	y = random.randint (-screen_height + maximum_ball_radius, screen_height - maximum_ball_radius)
	dx = random.randint (minimum_ball_dx, maximum_ball_dx)
	dy = random.randint(minimum_ball_dy, maximum_ball_dy)
	radius = random.randint(minimum_ball_radius, maximum_ball_radius)
	color = (random.random(), random.random(), random.random()) 
	random_ball = Ball(x, y, dx, dy, radius, color)
	BALLS.append(random_ball)



#part 2
#loop
def move_all_balls():
	for ball in BALLS:
		ball.move(screen_width, screen_height)
#part 3
#collision
def collide (ball_a, ball_b):
	if ball_a==ball_b: 
		return False
	if ball_a == button or ball_b == button:
		return False
	d= math.sqrt(math.pow(ball_a.xcor() - ball_b.xcor(), 2) + math.pow(ball_a.ycor()- ball_b.ycor(), 2))

	if ball_a.r + ball_b.r >= d:
		print("collide")
		return True

	else :
		return False

#part 4
#check if all balls collision
def check_all_balls_collision ():
	global running
	all_balls=[]
	all_balls.append(my_ball)
	for ball in BALLS:
		all_balls.append(ball)

	for ball_a in all_balls:
		for ball_b in all_balls:
			if collide(ball_a, ball_b):
				x = random.randint( -screen_width + maximum_ball_radius, screen_width - maximum_ball_radius)
				y = random.randint (-screen_height + maximum_ball_radius, screen_height - maximum_ball_radius)
				dx = random.randint (minimum_ball_dx, maximum_ball_dx)
				dy = random.randint(minimum_ball_dy, maximum_ball_dy)
				r = random.randint(minimum_ball_radius, maximum_ball_radius)
				color = (random.random(), random.random(), random.random()) 

				while dx == 0:
					dx = random.randint (minimum_ball_dx, maximum_ball_dx)
				
				while dy == 0:
					dy = random.randint(minimum_ball_dy, maximum_ball_dy)

	#Determine which ball is smaller.
				if ball_a.r< ball_b.r:
					if ball_a==my_ball:
						turtle.pu()
						turtle.goto(-300,200)
						turtle.write("GAME OVER" , font=("Comic Sans MS",80 , "normal"))
						running = False
					
					else:	
						ball_a.new_Ball(x,y,dx,dy,r,color)
						ball_b.r += 7
						ball_b.shapesize(ball_b.r/10)
				elif ball_a.r >ball_b.r:
					if ball_b == my_ball:
						turtle.pu()
						turtle.goto(-300, 200)
						turtle.write("GAME OVER" , font=("Comic Sans MS", 80, "normal"))
						running = False
					
					else:
						ball_b.new_Ball(x,y,dx,dy,r,color)
						ball_a.r += 7 
						ball_a.shapesize(ball_a.r/10)
#part 5 Movearound

def movearound ():
	X = turtle.getcanvas().winfo_pointerx() - screen_width*2
	Y = screen_height*1.4 - turtle.getcanvas().winfo_pointery()
	#print(X,Y)
	my_ball.goto (X, Y)
	my_ball.clear()
	my_ball.pencolor("black")
	my_ball.write(y_name ,align = "center", font=("Ariel",20, "normal"))

def replay(x,y):
	screen_width = turtle.getcanvas().winfo_width()/2
	screen_height = turtle.getcanvas().winfo_height()/2
	print("replay")
	my_ball.new_Ball(0,0 ,10,10, 20, "red")

#random ball
	for ball in BALLS:
		x = random.randint( -screen_width + 100, screen_width - 100)
		y = random.randint (-screen_height + 70, screen_height - 70)
		radius = random.randint(minimum_ball_radius, maximum_ball_radius)
		ball.goto(x,y)
		ball.r = radius
		ball.shapesize(radius/10)

	for ball in BALLS:
		ball.st()
	my_ball.st()
	
	global running
	running= True
	button.ht()
	turtle.clear()

	while running==True :
		screen_width = turtle.getcanvas().winfo_width()/2
		screen_height = turtle.getcanvas().winfo_height()/2
		movearound() 
		move_all_balls()
		check_all_balls_collision()
		turtle.update()

		my_ball.clear()
		my_ball.pencolor("black")
		my_ball.write(y_name ,align = "center", font=("Ariel",20, "normal"))
		time.sleep (.1)


	for ball in BALLS:
		ball.ht()
	my_ball.ht()
	my_ball.clear()
	#replay button
	button.showturtle()	
	turtle.update()
#part 6
while running==True :
	screen_width = turtle.getcanvas().winfo_width()/2
	screen_height = turtle.getcanvas().winfo_height()/2


	movearound() 
	move_all_balls()
	check_all_balls_collision()
	turtle.update()


	my_ball.clear()
	my_ball.pencolor("black")
	my_ball.write(y_name ,align = "center", font=("Ariel",20, "normal"))
	time.sleep (.1)


for ball in BALLS:
	ball.ht()
my_ball.ht()
my_ball.clear()
#replay button
button.showturtle()	
button.onclick(replay)
turtle.update()

turtle.mainloop()