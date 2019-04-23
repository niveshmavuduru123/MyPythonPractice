def getGrades(grade, size):
	for n in range(size):
		num = int(input("Enter a number : "))
		grade.append(num)

def getAverage(grades, size):
	total = 0
	for n in range(size):
		total = total + grades[n]
	a = total / size
	return a

def countlettergrades(grades, size, na, nb, nc, nd, nf): 
	'How to pass na, nb, nc, nd, nf by reference?'
	for n in range(size):
		if grades[n]>=90:
			na = na+1
		elif grades[n]>=80:
			nb = nb+1
		elif grades[n]>=70:
			nc = nc+1
		elif grades[n]>=60:
			nd = nd+1
		else:
			nf = nf+1

	return na, nb, nc, nd, nf


def printdata(average, na, nb, nc, nd, nf):
	print(f"Average : {average}")
	print(f"Number of A's {na}")
	print(f"Number of B's {nb}")
	print(f"Number of C's {nc}")
	print(f"Number of D's {nd}")
	print(f"Number of F's {nf}")





size = 5
grades = []
average = 0.0
na=0
nb=0
nc=0
nd=0
nf=0
getGrades(grades,size)
average  = getAverage(grades,size)
na, nb, nc, nd, nf = countlettergrades(grades,size, na, nb, nc, nd, nf)
printdata(average, na, nb, nc, nd, nf)