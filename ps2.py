###### this is the second .py file ###########

####### write your code here ##########


import numpy as np

k= (input().split(" "))

print(k)
if len(k)!=3:
	print("Wrong number of arguments")
	exit()
for i in range(3):
	k[i]= int(k[i])
	if k[i]<1 or k[i]>150:
		print("Wrong input")
		exit()

encrypt= input()
if len(encrypt) <1 or len(encrypt)>150:
	print("Wrong input")
	exit()

