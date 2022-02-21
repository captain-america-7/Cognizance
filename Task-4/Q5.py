#Created and developed by Arntej
#code to print a pattern
n=5       #n is no of line
k = n - 1 #k is no of spaces
for i in range(0, n):
	for j in range(0, k):
		print(end=" ")
	k = k - 1
	for j in range(0, i+1):
		print("* ", end="")
	print("\r")


