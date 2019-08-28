import sys
a = int(input("Enter the 1st no.: "))
b = int(input("Enter the 2nd no.: "))
if(a%b == 0):
	print("The 1st no is divisible by the second no.!")
elif(b%a == 0):
	print("The 2nd no is divisible by the 1st no.!")
else:
	print("The no. s are not divisible by each other! ")
