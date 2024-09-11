# Braden Leach
# Sep 11 2024
# String Concatenation

# Part 1
# Use concatenation to build and display a string that displays which city and state you live in
state = 'michigan '
city = 'buckely, '
full_location = city + state

print ("Hello, I am from: " + full_location)
# Part 2
# Create a custom message that welcomes the user by first name to a game you created
# Create one variable to store the user's first name
# Create another variable that stores the welcome message
# Use concatenation to create the customized message
first_name = input('what is your name: (example: Jack)\n')
message = 'this is my game!'
print (f'welcome, {first_name} {message}')

# Part 3
# Assign a number to your age variable
# Use the built-in Python str( ) function to convert your age to a string (when doing concatenation)
# Use concatenation to display a sentence that tells us your first name and age

#with an input
age = input('what is your age: (example: 17)\n')
first_name = input('what is your name: (example: Jack)\n')
full_message = first_name + ' your are: ' + age
print('hello, ' + full_message + '')

# Part 4
# Use an f-string to build and display a string that contains your first name, last name, and your height in inches
first_name = 'braden'
last_name = 'leach'
height = 69.6
print(f'My first name is {first_name} and my last name is {last_name} and my heigh in inches is {height}')