"""
#exercise 1:
import turtle
for i in range (5):
	turtle.fd (300)
	turtle.right(144)
turtle.mainloop()
"""
"""
#extra
import turtle
import random


for i in range (5):
	turtle.pensize(15)
	turtle.fd (300)
	turtle.right(144)
	R = random.random()
	G = random.random()
	B = random.random()
	turtle.color(R, G, B)

turtle.mainloop()
"""
"""
#exercise 2:
import turtle
turtle.fillcolor("black")
turtle.begin_fill()
for i in range (2):
	turtle.fd(100)
	turtle.right(90)
	turtle.fd(75)
	turtle.right(90)

turtle.end_fill()

turtle.fillcolor("black")
turtle.begin_fill()
turtle.goto(0, -75)
turtle.fd(100)
turtle.right(120)
turtle.fd(90)
turtle.right(113)
turtle.fd(90)

turtle.end_fill()
turtle.mainloop()
"""
# #exercis 3:
# import turtle 

# turtle.register_shape("duck.gif")
# turtle.shape("duck.gif")

# turtle.mainloop()

"""
#exercise 4:
#part 1:
import turtle
turtle.pensize(1)
turtle.forward(150)
turtle.pensize(0)
turtle.right(45)
turtle.fd(85)
turtle.right(90)
turtle.fd(75)
turtle.home())
turtle.mainloop()
"""
# #part 2:
# import turtle

# for i in range (360):
# 	turtle.right(i)
# 	turtle.forward(150)
# 	turtle.right(45)
# 	turtle.fd(85)
# 	turtle.right(90)
# 	turtle.fd(30)
# 	turtle.penup()
# 	turtle.home()
# 	turtle.pendown()
	

# turtle.mainloop()