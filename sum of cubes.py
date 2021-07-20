import sys
a = int(input("Enter a no.: "))
b = 0
if(a < 0):
	print("Enter a positive no.")
else:	
	for i in range (0,a+1):
    	b = b + (i*i*i)
	print ("The sum of cubes of no.s is:", b)
