from array import *
arr =[[2,3,1,5,0],[7,1,5,3,1],[2,5,7,8,1],[0,1,5,0,1],[3,4,9,1,5]]
for i in arr:
	for j in i:
		print(j,end=" ")
	print()

print()
for i in range(0,5):
	for j in range(0,5):
		if(i<= j):
			print(arr[i][j],end=" ")
		else:
			print(" ", end = " ");
	print()
