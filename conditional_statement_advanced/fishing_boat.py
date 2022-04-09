# Tony and his friends love to go fishing and are so passionate about fishing that they decide to go fishing by boat. 
# The price for renting a boat depends on the season and the number of fishermen:
# Depending on the season:
# ⦁ The price for renting the ship in the spring is 3000 BGN;
# ⦁ The price for renting the ship in summer and autumn is 4200 BGN;
# ⦁ The price for renting the ship in winter is 2600 BGN.
# Depending on the number of groups there is a different discount:
# ⦁ If the group is up to 6 people inclusive - 10% discount;
# ⦁ If the group is from 7 to 11 people inclusive - discount of 15%;
# ⦁ If the group is from 12 upwards - 25% discount.
# Fishermen enjoy an additional 5% discount if they are an even number, unless it is autumn - then they do not have an additional discount,
# which is accrued after deducting the discount according to the above criteria.
# Write a program to calculate whether fishermen will raise enough money.

# Entrance
# Three lines are read from the console:
# ⦁ Group budget - integer;
# ⦁ Season - text: "Spring", "Summer", "Autumn" or "Winter";
# ⦁ Number of fishermen - integer.

# Input
# 3000
# Summer
# 11

# Exit
# Print the following on the console:
# ⦁ If the budget is sufficient:
# "Yes! You have {the rest of the money} left."
# ⦁ If the budget is NOT sufficient:
# "Not enough money! You need {the amount that is not enough} leva."
# Amounts must be formatted to two decimal places.

budget = int(input())
season = input()
number_of_fisherman = int(input())
boat_rent = 0
if season == 'Spring':
    boat_rent = 3000
elif season == 'Summer'or season == 'Autumn':
    boat_rent = 4200
elif season == 'Winter':
    boat_rent =2600
if number_of_fisherman <= 6:
    boat_rent = boat_rent * 0.9
elif number_of_fisherman <= 11:
    boat_rent = boat_rent * 0.85
else:
    boat_rent = boat_rent * 0.75
if season != "Autumn" and number_of_fisherman % 2 == 0:
    boat_rent = boat_rent * 0.95
difference = abs(budget - boat_rent)
if budget >= boat_rent:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
