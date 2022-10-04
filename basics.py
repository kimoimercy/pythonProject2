print("Hello World")
# this is how to print a triangle
print("   /|")
print("  / |")
print(" /  |")
print("/___|")
# variables and data types
character_name = "Mercy"
character_age = "21"
print("there once was a girl called " + character_name + " ,")
print("she was " + character_age + " years old.")
print("she liked being " + character_age + " years old")
print("but she did not like the name " + character_name + " .")
# working with strings

print("King\nAcademy")
# how to insert a quote
print("king\"Academy")
msg = "King Academy"
print(msg + " is cool")

# working with functions
phrase = "King Academy"
print(phrase.lower())  # converts string to lowercase
print(phrase.upper())  # converts string to uppercase
print(phrase.isupper())  # checks for uppercase characters
print(phrase.upper().isupper())  # converts my string to uppercase and checks if it is upper case
print(len(phrase))  # how many characters are in the string
# getting individual characters inside a string
print(phrase[0])  # we start counting from 0

# index function tells us where a specific character will be in our string
print(phrase.index("a"))
# replace - replaces words or letters in our string
print(phrase.replace("King", "Queen"))
