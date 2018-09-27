###### this is the second .py file ###########

####### write your code here ##########

######Code for problem 2######

import numpy as np

#Getting input from user
k= (input().split(" "))

#checking for boundry conditions
if len(k)!=3:
	print("Wrong number of arguments")
	exit()
for i in range(3):
	k[i]= int(k[i])
	if k[i]<1 or k[i]>150:
		print("Wrong input")
		exit()

#getting encrypted message from user
en= input()
if len(en) <1 or len(en)>150:
	andprint("Wrong input")
	exit()


#list to store alphabet of all three groups and their index
g1=[]
g2=[]
g3=[]
i1=[]
i2=[]
i3=[]

#for entire message
for i in range(len(en)):
	#if it lies in 1st group the add to list one
	if en[i]>='a' and en[i]<='i':
		g1.append(en[i])
		i1.append(i)
	#if it lies in 2nd group the add to list two	
	elif en[i]>='j' and en[i]<='r':
		g2.append(en[i])
		i2.append(i)
	#if it lies in 3rd group the add to list three
	elif (en[i]>='s' and en[i]<='z') or en[i]=='_':
		g3.append(en[i])
		i3.append(i)
	#else the message contains some wrong character
	else:
		print("Wrong input")
		exit()



#rotating list g1 by k1
newg1 = (g1[len(g1) - k[0]:len(g1)]  
                 + g1[0:len(g1) - k[0]])
#rotating list g2 by k2 
newg2 = (g2[len(g2) - k[1]:len(g2)]  
                 + g2[0:len(g2) - k[1]]) 
#rotating list g3 by k3
newg3 = (g3[len(g3) - k[2]:len(g3)]  
                 + g3[0:len(g3) - k[2]]) 

#to store decrypted message
de= [None]* len(en)

#merging all the three list
#merging list one
for i in range(len(i1)):
	de[i1[i]]= newg1[i]
#merging list two	
for i in range(len(i2)):
	de[i2[i]]= newg2[i]
#merging list three	
for i in range(len(i3)):
	de[i3[i]]= newg3[i]	


#joining the list to form a string
dec= "".join(de)
#dsiplaying the decrypted message
print(dec)




