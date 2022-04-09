# A young programmer has a certain budget and free time in a given season. Write a program that accepts the budget and the season at the entrance,
# and at the exit to earn where the programmer will rest and how much he will spend.nThe budget determines the destination, and the season
# - how much of the budget will spend. If it is summer he will rest at the campsite and in the winter at a hotel. 
# If he is in Europe, regardless of the season, he will stay in a hotel. Each campsite or hotel, according to the destination, has 
# its own price, which corresponds to a certain percentage of the budget:
# ⦁ At BGN 100 or less - somewhere in Bulgaria:
# ⦁ Summer - 30% of the budget;
# ⦁ Winter - 70% of the budget.
# ⦁ At BGN 1,000 or less - somewhere in the Balkans:
# ⦁ Summer - 40% of the budget;
# ⦁ Winter - 80% of the budget.
# ⦁ For more than BGN 1,000 - somewhere in Europe:
# ⦁ When traveling in Europe, regardless of the season, you will spend 90% of the budget.

# Entrance
# The input is readable by the console and consists of two lines entered by the user:
# ⦁ Budget - real number;
# ⦁ One of the two possible seasons - "summer" or "winter".

# Exit
# Two lines must be printed on the console:
# ⦁ "Somewhere in" between "Bulgaria", "Balkans" and "Europe"
# ⦁ "{Type of holiday} - {Amount spent}":
# ⦁ Holidays can be between "Camp" and "Hotel"
# ⦁ The amount must be formatted to the second decimal place

# Input 
# 50
# summer

# budget = float(input())
# season = input()
# destination = " "
# type_of_location = " "
# total_price = 0
# if budget <= 100:
#     destination = 'Bulgaria'
#     if season == 'summer':
#         total_price = budget * 0.30
#         type_of_location = 'Camp'
#     elif season == 'winter':
#         total_price = budget * 0.70
#         type_of_location = 'Hotel'
# elif budget <= 1000:
#     destination = 'Balkans'
#     if season == 'summer':
#         total_price = budget * 0.40
#         type_of_location = 'Camp'
#     elif season == 'winter':
#         total_price = budget * 0.80
#         type_of_location = 'Hotel'
# else:
#     destination = 'Europe'
#     total_price = budget * 0.9
#     type_of_location = 'Hotel'
# print(f"Somewhere in {destination}")
# print(f"{type_of_location} - {total_price:.2f}")
