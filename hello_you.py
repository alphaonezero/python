# Ask user for their name
name = input("What is your name?: ")

# Ask user for age
age = input("How old are you?: ")

# Ask user for city
city = input("What city are you from?: ")

# Ask user for their favorite hobby
hobby = input("What is your favorite hobby?: ")

# Create output text
string = "Your name is {} and you are {} years old. You live in {} and love to {}."
output = string.format(name, age, city, hobby)

# Print output to screen
print("-"*10+"Results"+"-"*10)
print(output)
