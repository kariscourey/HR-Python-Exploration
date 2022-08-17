message = "This is a string in a Python file"
some_number = 1928

print("This message is", message)
print("This number is", some_number)

number_three = 3
string_three = "3"
print(number_three)
print(string_three)

print(number_three == string_three)

response = input("How many walls in room? ")
print("You typed: ", response)
print("The value is a ", type(response))

num_walls = int(response)
print("My room has ", num_walls+1, " walls")

title = "Dr."
name = "Syed"
combined = title + " " + name
print(combined)
