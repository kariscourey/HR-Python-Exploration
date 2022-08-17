age_string = input("How old are you? ")
age = int(age_string)
print("Next year, you'll be", age + 1, "years old")

name = input("Name? ")

print() # Print nothing
print(name) # Print the value in name
print("!") # Print an exclamation
print("Hello,", name) # Print hello and then the value in name

print(1, 2, 3, 4, 5, "and that's it!")

# input("How old are you?", "Extra thing")

int("34")

age_string = input("How old are you? ")
age = int(age_string)

name = input("Please type name: ")

if len(name) > 8:
    print("You have a long name!")
else:
    print("You have a short name!")
