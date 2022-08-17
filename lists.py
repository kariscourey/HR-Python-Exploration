my_list = ["Evander", 22, True]
print(my_list)

days = [
    "sun",
    "mon",
    "tues",
    "wed",
    "thurs",
    "fri",
    "sat"
]

print(days)

fav_foods = []

food = input("Fav food? ")
fav_foods.append(food)

food = input("Fav food? ")
fav_foods.append(food)

num_foods = len(fav_foods)
print("That's", num_foods, "of your fav foods.")

print("first day is", days[0])

days[3] = "hump day!"
print(days)

days[5] = "FriYAY!"
print(days)
