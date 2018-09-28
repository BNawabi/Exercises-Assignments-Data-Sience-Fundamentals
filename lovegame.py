print("Welcome to the Love Test!")

my_name = input("What is your name? ")
lovers_name = input("What is your lovers name? ")

my_name_lower_strip = my_name.lower().strip()
lovers_name_lower_strip = lovers_name.lower().strip()

all_names = my_name_lower_strip + lovers_name_lower_strip 

names_len = len(all_names)

if names_len == 10:
	print("This is a perfect match!")

elif names_len >= 8:
	print("You can find better..")

else:
	print("Search for someone else.")