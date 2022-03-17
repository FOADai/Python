n=int(input())

L=[]
for i in range(0,n):
	s=input().split()
	L.append(s)
L = [list(map(int, lst)) for lst in L]
print(L,type(L[0][1]))	
flag=0 

for i in L:
	for j in range(1,len(L)):
		if((i[1]>=L[j][1]) and (i[0]<L[j][0])):
	 	 flag=1
	 
if flag==1:
	print("happy irsa")
else:
	print("poor irsa")