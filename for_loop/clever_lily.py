# Lily is already N years old. She receives a gift for each of her birthdays.
# ⦁ For odd birthdays (1, 3, 5 ... n) receives toys.
# ⦁ For even birthdays (2, 4, 6 ... n) receives money.
# For the second birthday he receives BGN 10.00, as the amount increases by BGN 10.00, for each subsequent even birthday (2 -> 10, 4 -> 20, 6 -> 30 ... etc.). 
# Over the years, Lily has secretly saved money. Lily's brother, in the years she receives money, takes BGN 1.00 from them. 
# Lily sold the toys received over the years, each for P levs and added the amount to the money saved. 
# With the money she wanted to buy a washing machine for X leva. Write a program to calculate how much money she has raised and whether she has enough to buy a washing
# machine.

# Entrance
# The program reads 3 numbers entered by the user in separate lines:
# ⦁ Lily's age - an integer in the range [1 ... 77]
# ⦁ The price of the washing machine - a number in the range [1.00 ... 10 000.00]
# ⦁ Unit price of a toy - an integer in the range [0 ... 40]

# Exit
# Print one line on the console:
# ⦁ If Lily's money is enough:
# Yes "Yes! {N}" - where N is the cash balance after purchase
# ⦁ If the money is not enough:
# "" No! {M} "- where M is the amount that is not enough
# The numbers N and M must be formatted to the second decimal place.

# Input
# 10
# 170.00
# 6

ages = int(input())
laundry_price = float(input())
toy_price = int(input())
total_money = 0
total_toys = 0
birthday_money = 0
for current_age in range(1, ages + 1):
    if current_age % 2 != 0:
        total_toys += 1
    else:
        birthday_money += 10
        total_money += birthday_money - 1
total_money += total_toys * toy_price
difference = abs(total_money - laundry_price)
if total_money >= laundry_price:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")
