age = 23
cash = 5

if age > 17 and cash > 8:
    print("You can buy a ticket")
    print("How many?")
else:
    print("You may not buy a ticket")
    print("Candy?")

print("Thank you")

n = 12
x = 17
o = 100

if n > 10 and x < 15 or o >= 100:
    print("yes")

age = 19

if age > 12 and age < 20:
    is_teenager = True
else:
    is_teenager = False

if is_teenager:
    print("Tiktok?")
else:
    print("Facebook?")

this_is_false = 3 < 2 # 3 < 2 returns false, so this_is_false returns false
print(this_is_false)

if "":
    print("Empty string is considered true")
else:
    print("Empty string is considered false")

if 0:
    print("0 is considered true")
else:
    print("0 is considered false")

age = 23
cash_on_hand = 5

if age > 17 and cash_on_hand > 8:
    print("You can buy a lottery ticket.")
    print("How many would you like?")
elif age > 17 and cash_on_hand <= 8:
    print("You don't have enough money.")
    print("Please, come back when you get more.")
else:
    print("You may not buy a lottery ticket.")
    print("Can I interest you in some candy?")

print("Thank you for your patronage.")
