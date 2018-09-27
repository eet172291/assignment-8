###### this is the second .py file ###########

####### write your code here ##########


import numpy as np

k= (input().split(" "))

if len(k)!=3:
	print("Wrong number of arguments")
	exit()
for i in range(3):
	k[i]= int(k[i])
	if k[i]<1 or k[i]>150:
		print("Wrong input")
		exit()

en= input()
if len(en) <1 or len(en)>150:
	andprint("Wrong input")
	exit()

g1=[]
g2=[]
g3=[]
i1=[]
i2=[]
i3=[]

for i in range(len(en)):
	if en[i]>='a' and en[i]<='i':
		g1.append(en[i])
		i1.append(i)
	elif en[i]>='j' and en[i]<='r':
		g2.append(en[i])
		i2.append(i)
	elif (en[i]>='s' and en[i]<='z') or en[i]=='_':
		g3.append(en[i])
		i3.append(i)
	else:
		print("Wrong input")
		exit()




newg1 = (g1[len(g1) - k[0]:len(g1)]  
                 + g1[0:len(g1) - k[0]]) 
newg2 = (g2[len(g2) - k[1]:len(g2)]  
                 + g2[0:len(g2) - k[1]]) 
newg3 = (g3[len(g3) - k[2]:len(g3)]  
                 + g3[0:len(g3) - k[2]]) 

de= [None]* len(en)

for i in range(len(i1)):
	de[i1[i]]= newg1[i]	
for i in range(len(i2)):
	de[i2[i]]= newg2[i]	
for i in range(len(i3)):
	de[i3[i]]= newg3[i]	


dec= "".join(de)
print(dec)




