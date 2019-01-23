
# #problem1:
# #1:
# print("Almog")

# #2:
# for index in range(3):
# 	print("Almog")

# #3:
# for index in range(100):
# 	print("Almog") 
	

"""
#problem2:
#part1:
number1 = 8
print(number1)

#part2:
number2 = number1/2
print(number2)
"""

"""
#problem3:
#parrt1:
numbers= [1, 3 ,5]
for num in numbers :
	print (num)

#part2:
for num2 in numbers :
	print (num2)
	print (num2 * 2)

#part3:
sum = 0
for num3 in numbers :
	print (num3)
	print (num3 * 2)
	sum += num3
print (sum)
"""

"""
#problem4:
#1:
import turtle
turtle.goto(100,100)
turtle.mainloop()

#how to mke the line disappear:
import turtle
turtle.penup ()
turtle.goto(100,100)
turtle.mainloop()
"""

"""
#make squre on the screen
import turtle
turtle.penup ()
turtle.goto(100,100)
turtle.pendown ()
turtle.goto (100,0) 
turtle.goto (0,0)
turtle.goto (0,100)
turtle.goto (100,100)
turtle.mainloop()
"""

"""
#fiil squre
import turtle
turtle.penup ()
turtle.goto(100,100)
turtle.pendown ()
turtle.color( "red")
turtle.begin_fill()
turtle.goto (100,0) 
turtle.goto (0,0)
turtle.goto (0,100)
turtle.goto (100,100)
turtle.end_fill()
turtle.mainloop()
"""

"""
#create circle
import turtle
turtle.penup()
turtle.goto(300,100)
turtle.pendown ()
turtle.circle(100)
turtle.mainloop()
"""

#olympic rings
import turtle
turtle.penup()
turtle.goto(300,100)
turtle.pendown ()
turtle.color("red")
turtle.pensize (20)
turtle.circle(100)

#black circle
turtle.penup()
turtle.goto(50,100)
turtle.pendown ()
turtle.color("black")
turtle.pensize (20)
turtle.circle(100)

#blue circle
turtle.penup()
turtle.goto(-200,100)
turtle.pendown ()
turtle.color("blue")
turtle.pensize (20)
turtle.circle(100)

#green circle
turtle.penup()
turtle.goto(175,0)
turtle.pendown ()
turtle.color("green")
turtle.pensize (20)
turtle.circle(100)

#yellow circle
turtle.penup()
turtle.goto(-80,0)
turtle.pendown ()
turtle.color("yellow")
turtle.pensize (20)
turtle.circle(100)

turtle.mainloop()