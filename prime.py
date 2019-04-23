count = 0
n = 1
j = 1
for n in range(1,100):
	if n==2:
		print(f"{n} is a prime number")
	for j in range(2,n):
		if n%j != 0:
			count = count+1
		else:
			count = 0
			break
	if(count!=0):
		print(f"{n} is a prime number")

