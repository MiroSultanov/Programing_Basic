# The restaurant opens its doors and offers several menus at preferential prices:
# ⦁ Chicken menu - BGN 10.35.
# ⦁ Fish menu - BGN 12.40.
# ⦁ Vegetarian menu - BGN 8.15.
# Write a program that calculates how much it will cost a group of people to order food to take home.
# The group will also order a dessert, the price of which is equal to 20% of the total bill (excluding delivery).
# The delivery price is BGN 2.50 and is finally charged.

# Entrance
# 3 lines are read from the console:
# Number of chicken menus - integer in the range [0… 99]
# Number of fish menus - integer in the range [0… 99]
# Number of vegetarian menus - integer in the range [0… 99]

# Exit
# Print one line on the console: "{order price}"

chicken_menu = int(input())
fish_menu = int(input())
vegan_menu = int(input())

price_for_chicken_menu = chicken_menu * 10.35
price_for_fish_menu = fish_menu * 12.40
price_for_vegan_menu = vegan_menu * 8.15
total_sum = price_for_chicken_menu + price_for_fish_menu + price_for_vegan_menu
price_for_desert = 0.2 * total_sum
delivery = 2.50
total_sum_order = total_sum + price_for_desert + delivery
print(f"{total_sum_order:.2f}")
