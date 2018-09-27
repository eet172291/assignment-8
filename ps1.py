###### this is the first .py file ###########

####### write your code here ##########



import numpy as np

def get_dim(cell, i, j):
	x= [-1, 0, 1, 0]
	y= [0, -1, 0, 1]
	dim=-1
	n, m = np.array(cell).shape
	if cell[i][j]== 'D':
		return dim
	else:
		dim=1
	num=1
	while True:
		for search in range(4):
			newi= i+num*x[search]
			newj= j+num*y[search]
			if newi<0 or newi >=n or newj<0 or newj >=m or cell[newi][newj]== 'D':
				return dim
		dim= dim+4
		num= num+1

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

dim= [ [ None for y in range( m ) ] for x in range( n ) ]

for i in range(n):
	for j in range(m):
		dim[i][j]= get_dim(cell, i, j)
large= dim[0][0]
sec_large= dim[0][0]
for i in range(n):
	for j in range(m):
		if dim[i][j]>= large:
			sec_large= large			
			large= dim[i][j]

print(large, sec_large)		

			
