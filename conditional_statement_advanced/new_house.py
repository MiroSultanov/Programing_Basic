# Marin and Nelly are buying a house not far from Sofia. Nelly loves flowers so much that she persuades you to write a program that calculates how much it will 
# cost them to plant a certain number of flowers and whether the available budget will be enough. Different flowers have different prices:

# flower      Rose      Dahlia     Tulip     Narcissus      Gladiolus
# Price        5        3.80       2.80         3              2.50

# There are the following discounts:
# ⦁ If Nelly buys more than 80 Roses - 10% discount from the final price;
# ⦁ If Nelly buys more than 90 Dahlias - 15% discount from the final price;
# ⦁ If Nelly buys more than 80 Tulips - 15% discount from the final price;
# ⦁ If Nelly buys less than 120 Narcissus - the price goes up by 15%;
# ⦁ If Nelly Buys less than 80 Gladiolus - the price goes up by 20%.
# 3 lines are read from the console:
# ⦁ Type of flowers - text with options "Roses", "Dahlias", "Tulips", "Narcissus" or "Gladiolus";
# ⦁ Number of flowers - integer;
# ⦁ Budget is an integer.
# To print on the console in one line:
# ⦁ If their budget is enough - "Hey, you have a great garden with {number of flowers} {type of flowers} and {remaining amount} leva left.";
# ⦁ If their budget is NOT enough - "Not enough money, you need {the amount needed} leva more.".
# The amount should be formatted to the second decimal place.


type_of_flower = input()
number_of_flowers = int(input())
budget = int(input())
price_per_flower = 0

if type_of_flower == "Roses":
    price_per_flower = 5
    if 80 < number_of_flowers:
        price_per_flower *= 0.9
elif type_of_flower == "Dahlias":
    price_per_flower = 3.80
    if 90 < number_of_flowers:
        price_per_flower *= 0.85
elif type_of_flower == "Tulips":
    price_per_flower = 2.80
    if 80 < number_of_flowers:
        price_per_flower *= 0.85
elif type_of_flower == "Narcissus":
    price_per_flower = 3
    if 120 > number_of_flowers:
        price_per_flower += price_per_flower * 0.15
elif type_of_flower == "Gladiolus":
    price_per_flower = 2.50
    if 80 > number_of_flowers:
        price_per_flower += price_per_flower * 0.2

total_sum = price_per_flower * number_of_flowers
money_left = abs(total_sum - budget)

if budget >= total_sum:
    print(f"Hey, you have a great garden with {number_of_flowers} {type_of_flower} and {money_left:.2f} leva left.")
else:
    print(f"Not enough money, you need {money_left:.2f} leva more.")
