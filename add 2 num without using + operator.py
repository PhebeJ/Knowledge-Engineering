 import sys
a = int(input("Enter the first no.: "))
b = int(input("Enter the secon no.: "))
while(b !=0):
	carry = a & b
	a = a ^ b
	b = carry << 1
print (a)    

