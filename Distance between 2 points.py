import sys
import math
x1= int(input("Enter the x coordinate of the first point: " ))
y1= int(input("Enter the y coordinate of the first point: "))
x2=int(input("Enter the x coordinate of the second point: "))
y2= int(input("Enter the y coordinate of the second point: "))
p = x1-y1
q=x2-y2
l=p**2 + q**2
m=math.sqrt(l)
print ("Distance between the points is ", m)
