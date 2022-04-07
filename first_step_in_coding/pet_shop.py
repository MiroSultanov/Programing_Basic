# Write a program that calculates the cost of buying dog and cat food. The food is bought from a pet store, as one package of dog food costs BGN 2.50, 
# and a package of cat food costs BGN 4.

# Entrance
# 2 lines are read from the console:
# ⦁ Number of packages of dog food - integer in the range [0… 100]
# ⦁ Number of packages of cat food - integer in the range [0… 100]

# Exit
# The following is printed on the console:
# "{final amount} lv."

number_of_dog_food = int(input())
price_for_dog_food = number_of_dog_food * 2.50

number_of_cat_food = int(input())
price_for_cat_food = number_of_cat_food * 4

total_sum = price_for_cat_food + price_for_dog_food
print(f'{total_sum} lv.')
