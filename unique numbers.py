 import sys
a = int(input("Enter the range:"))
arr = []
p = 0
print("Enter the no.s")
for i in range (a):
	b = int(input())
	arr.append(b)
for i in range (a):
	for j in range (i + 1, a):
    	if(arr[i] == arr[j]):
        	p = 1
    	else:
        	continue
if (p == 1):
	print("The numbers are not unique")
else:
	print("The numbers are unique!")
 
