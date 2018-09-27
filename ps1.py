###### this is the first .py file ###########

####### write your code here ##########

####### Code for problem 1 ######

import numpy as np

#function to find dimension of each cell
def get_dim(cell, i, j):
	#vectors that search in all 4 direction
	x= [-1, 0, 1, 0]
	y= [0, -1, 0, 1]
	dim=-1
	#getting shape of the matrix
	n, m = np.array(cell).shape
	#if the cell is dull cell then its dimension is -1
	if cell[i][j]== 'D':
		return dim
	#else dimension is 1
	else:
		dim=1
	num=1
	#searching for largest cross around the cell
	while True:
		#checking for all 4 neighbour
		for search in range(4):
			newi= i+num*x[search]
			newj= j+num*y[search]
			#if any of the for neighbour is missing or any one is a dull cell then return with the previous dimension
			if newi<0 or newi >=n or newj<0 or newj >=m or cell[newi][newj]== 'D':
				return dim

		#else dimension is increased by 4
		dim= dim+4
		num= num+1

#getting input from user
n= int(input("Enter n: "))
m= int(input("Enter m: "))
#checking for boundry condition
if n<2 or n>105 or m<2 or m>105:
	print("Wrong input")
	exit()
#getting the cells from user
cell= [ [ None for y in range( m ) ] for x in range( n ) ]

for i in range(n):
	s= input()
	for j in range(m):
		cell[i][j]=s[j]

#checking if the cells are valid
for i in range(n):
	for j in range(m):
		if cell[i][j]!= 'S' and cell[i][j]!= 'D':
			print("Wrong input")
			exit()
#list to store dimension of all the cells
dim= [ [ None for y in range( m ) ] for x in range( n ) ]


#getting the dimension of all cell one by one
for i in range(n):
	for j in range(m):
		dim[i][j]= get_dim(cell, i, j)

#to get largest and second largest cross
large= dim[0][0]
sec_large= dim[0][0]
#searching in the entire matrix, largest and second largest
for i in range(n):
	for j in range(m):
		if dim[i][j]>= large:
			sec_large= large			
			large= dim[i][j]

#displaying the result
print(large, sec_large)		

			
