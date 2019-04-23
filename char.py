import datetime
print("Getting input from the user")
print("---------------------------")
Name = input("Please enter your name : ")
Age = int(input("Please enter your age : "))
cur_year1 = datetime.datetime.now() #to access the current date year month hour minute second
cur_year = cur_year1.year
turn_old = 100 - Age
final_year = cur_year + turn_old

print(f"{Name} of {Age} will turn 100 in {final_year} year.")

copies = int(input("Enter number of copies : "))
for n in range(copies):
	print(f"{Name} of {Age} will turn 100 in {final_year} year.")
for n in range(copies):
	print(f"{Name} of {Age} will turn 100 in {final_year} year. \n")
