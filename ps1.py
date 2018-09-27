###### this is the first .py file ###########

####### write your code here ##########



import numpy as np

n= int(input("Enter n: "))
m= int(input("Enter m: "))
if n<2 or n>105 or m<2 or m>105:
	print("Wrong input")
	exit()

cell= [ [ None for y in range( m ) ] for x in range( n ) ]

for i in range(n):
	s= input()
	for j in range(m):
		cell[i][j]=s[j]
	
for i in range(n):
	for j in range(m):
		if cell[i][j]!= 'S' and cell[i][j]!= 'D':
			print("Wrong input")
			exit()

	
