# Ask user for name
name = input("what is ur name?: ")

# Ask user for age 
age = input("what is ur age?: ")

# Ask user for city
city = input("what city u live in?: ")

# Ask user what they enjoy
enjoy = input("wat do u enjoy doing?: ")

# Create output text
string = "ur name is {} , ur age is {} , u live in the {} city , u enjoy doing {}."
output = string.format(name,age,city,enjoy)

# Print output to screen

print(output)


