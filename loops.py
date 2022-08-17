months_in_year = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

for month in months_in_year: # Each value is assigned to "month" variable
    print(month)

print("months with names that have")
print("more than 8 letters: ")

for month in months_in_year:
    if len(month) > 8:
        print(month)

for num in range(5):
    print(num)

fav_foods = []

for num in range(3):
    food = input("Please tell me a fav food: ")
    fav_foods.append(food)

print("Thanks!")
for food in fav_foods:
    print(food)

# infinite = [1]
# for item in infinite:
#     print(item, len(infinite))
#     infinite.append(item + 1)
