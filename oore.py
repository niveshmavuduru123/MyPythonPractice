print("Odd or even")
print("-----------")
num = float(input("Enter a Number: "))
if num%2.0==0:
	print(f"{num} is an Even Number")
else:
	print(f"{num} is an Odd Number")
#checking for the multiple of 4.
if num%4 == 0:
	print(f"{num} is multiple of 4")
#Enter 2 numbers
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
if num1%num2 == 0:
	print(f"{num1} is divide by {num2}")
else:
	print(f"{num1} can not divided by {num2}")