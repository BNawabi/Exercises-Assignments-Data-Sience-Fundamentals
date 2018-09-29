# Billal Nawabi - Assignment 1

print("Welcome to the registration assignment!")

# this asks for the first name of the user
first_name = input("What is your first name? ")
print("Hey " + first_name + ", welcome to my program!")

# this asks for the last name of the user : only nawabi / Nawabi is a familiy member
last_name = input("What is your last name? ")
if "nawabi" in last_name:
	print("You are a family member!")

elif "Nawabi" in last_name:
	print("You are a family member!")

else: 
	print("You are not a family member.")

# this calculates the age of the user
year_now = 2018 
birth_year = input("What is your birth year? ")
birth_year_int = int(birth_year)
age = year_now - birth_year_int
print("You are " + str(age) + " years old.")

# this asks for the birth year of the user : the program could be run by 18+ years
if birth_year <= "2000":
	print("You are old enough for this program.")

else:
	print("WARNING: You are not old enough to enter. You will automatically exit now.")	
	exit()

# this calculates the length of the name and calculates the value
first_name_len = len(first_name)
last_name_len = len(last_name)

name_len = first_name_len + last_name_len

if name_len <= 10:
	name_len = 10

elif name_len > 10:
	name_len = 20

# this asks for the gender & ads and calculates the value
gender = input("Are you a male / female? ")
if "male" in gender:
	gender_int = 50

elif "female" in gender:
	gender_int = 50	

ads = input("Do you want to see some ads? Yes / No ")
if "yes" in ads:
	ads_int = 50

else: 
	ads_int = 0

value = name_len + gender_int + ads_int

print ("Your value is " + str(value))

# this is question 1 out of 2 / feedback
question_1 = input("Did you like this program?: Yes / No ")
if "yes" in question_1:
	print("Godthank, I did my best for you!")

else:
	print("Awh, screw you. I didn't like you anyway!")

# this is question 2 out of 2 / feedback
question_2 = input("Are you willing to come back again?: Yes / No ")
if "yes" in question_2:
	print("Cool, I will reserve a spot for you!")

else:
	print("What a shame, we can not be friends.")

print("Thank you for using my program. Goodbye.")
exit()



