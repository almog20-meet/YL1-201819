"""
#exercise 1:
a=[5,10,15,20,25]
def new_list():
	b=[(a[0]), (a[-1])]
	print b

new_list()
"""

"""
#exercise 2:
#1
a=[1,1,2,3,5,8,13,21,34,55,89]
rang= 5
type(rang)
for num in a :
	global user_type
	if num < rang:
		print (num)
""" 
"""
#extras A
a=[1,1,2,3,5,8,13,21,34,55,89]
b=[]
rang= 5
type(rang)
for num in a :
	global user_type
	if num < rang:
		b.append(num)
print b

#extras B
a=[1,1,2,3,5,8,13,21,34,55,89]
b=[]
rang= raw_input ("what yours range?")
type(rang)
for num in a :
	global user_type
	if num < rang:
		b.append(num)
print b


#exercise three:
a=[1,1,2,3,5,8,13,21,34,55,89]
b=[1,2,3,4,5,6,7,8,9,10,11,12,13]
c=[]
for num in a:
	if num in b:
		c.append(num)
print c
"""

#exercise four:
import math
import tkinter as tk
from tkinter import simpledialog

number = int(simpledialog.askstring("Input", "choose number!",
                                parent=tk.Tk()))
IsPrime = True
for i in range (2, number):
	if number % i == 0 :
		IsPrime= False
		
if IsPrime:
	print ("this is prime number")
else:
	print ("this is not a prime numbers")
