l = [1,1,2,3,5,8,13,21,34,55,89]
newlist = []
newlist2 = []
for n in l:
	if n<5:
		print(f"{n} \t")

#making a new list
for n in l:
	if n<5:
		newlist.append(n)

num = int(input("enter a number : "))
for n in l:
	if n<num:
		newlist2.append(n)

print(f"Newlist is : {newlist}")
print(f"Newlist2 is : {newlist2}")