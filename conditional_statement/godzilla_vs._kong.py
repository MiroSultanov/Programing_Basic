# Filming for the long-awaited film "Godzilla vs. Kong" begins. 
# Screenwriter Adam Wingard asks you to write a program to calculate whether the funds provided are enough to shoot the film. 
# The photos will require a certain number of extras, clothing for each extra and decor.
# It is known that:
# ⦁ The set for the film is worth 10% of the budget.
# ⦁ For more than 150 extras, there is a 10% discount on clothing.

# Entrance
# 3 lines are read from the console:
# ⦁ Movie budget - real number in the interval [1.00… 1000000.00]
# ⦁ Number of extras - integer in the range [1… 500]
# ⦁ Price for clothing of one extra - real number in the interval [1.00… 1000.00]

# Exit
# Two lines must be printed on the console:
# ⦁ If the money for the decor and clothes is more than the budget:
# ⦁ "Not enough money!"
# } "Wingard needs {money not enough for the movie} leva more."
# ⦁ If the money for the decor and the clothes is less than or equal to the budget:
# ⦁ "Action!"
# ⦁ "Wingard starts filming with {remaining money} left left."
# The result must be formatted to the second decimal place.

budget = float(input())
number_of_statists = int(input())
price_fer_dress_for_one_statist = float(input())
decor = budget * 0.1
price_for_dress = number_of_statists * price_fer_dress_for_one_statist
if number_of_statists > 150:
    price_for_dress *= 0.9
needed_money = decor + price_for_dress
difference = abs(needed_money - budget)
if needed_money > budget:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
