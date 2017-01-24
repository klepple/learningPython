#This program contains a list, for and while loops, and functions
#I will be creating a list of cats and playing around with it

my_cats = ["Nina", "Bozo", "Midnight"] #A list of cats
size = len(my_cats) #Original size of my list of cats

print "Hello! I'd like you to meet my cats:"

def print_cats(): #Function that prints out list of cats
	for i in range (len(my_cats)):
		print "\t - " + my_cats[i]
	
print_cats() #Calls print cats function
	
print "I own", len(my_cats), "cats... but I'd like to own more! How many cats should I own?"
new_cat_number = raw_input('>') #Accepts the user's input of how many cats
new_cat_number = int (new_cat_number) #Converts the string entered by the user to an integer

def check_cats(cat_number): #Function that checks the new number of cats
	check = False #Bool value
	while check == False: #Runs while check is false
		while (cat_number <= len(my_cats)): #Runs when less or equal to the existing number of cats
			print "Aw... c'mon, I want more cats! Please tell me how many cats I should own:"
			cat_number = raw_input('>')
			cat_number = int (cat_number)
	
		while (cat_number >= 10): #Runs when more or equal to 10
			print "Whoa! Okay, I'm not ready to own that many cats!! Please, less than 10 cats:"
			cat_number = raw_input('>')
			cat_number = int (cat_number)

		else: #Breaks out of the while loop once conditions are satisfied
			check = True
			return cat_number

checked_cat_number = check_cats(new_cat_number) #Calls check_cats function	

add_cats = checked_cat_number - len(my_cats) #Calculates how many more cats to add
	
print "Okay! I will get ", add_cats , " more cats!"

for i in range (add_cats):
	print "What should I name my new cat? It is new cat number", (i + 1)
	cat_name = raw_input('>')
	my_cats.append(cat_name) #Adds the new cat to my list of cats
	print "I have", len(my_cats), "cats now!"
	
print "Wow! I have so many cats now! Here are all my cats:"
print_cats()

print "I used to have only", size, "cats! Now I have", len(my_cats), "!"
print "I love all my cats, but", my_cats[0], "is my first cat, and is very special to me."
print "I hope that", ', '.join(my_cats[0:(size - 1)]), 
print "and" , my_cats[size - 1], "will love their new friends!"	
print "Thanks for your help! Good bye!"