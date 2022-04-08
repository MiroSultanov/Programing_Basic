# Peter wants to buy N video cards, M CPU and P number of RAM. If the number of video cards is greater than that of the processors, 
# it receives a 15% discount on the final bill. The following prices apply:
# ⦁ Video card - BGN 250 / pc.
# ⦁ Processor - 35% of the price of the purchased video cards / pc.
# ⦁ Memory frame - 10% of the price of the purchased video cards / pc.
# Calculate the amount needed to purchase the materials and calculate whether the budget will be enough.

# Entrance
# The entrance consists of four rows:
# ⦁ Peter's budget - a real number in the interval [0.0… 100000.0]
# ⦁ Number of video cards - integer in the range [0… 100]
# ⦁ Number of processors - integer in the range [0… 100]
# ⦁ The number of memory frames - integer in the range [0… 100]

# Exit
# 1 line is printed on the console, which should look like this:
# ⦁ If the budget is sufficient:
# "You have {residual budget} left left!"
# ⦁ If the amount exceeds the budget:
# "Not enough money! You need {necessary amount} left more!"
# Format the result to the second decimal place.

budget = float(input())
number_cards = int(input())
number_processor = int(input())
number_ram = int(input())
price_cards = number_cards * 250
price_processor = (price_cards * 0.35) * number_processor
price_ram = (price_cards * 0.1) * number_ram
total_price = price_ram + price_processor + price_cards
if number_cards > number_processor:
    total_price = total_price * 0.85
if budget >= total_price:
    rest_money = budget - total_price
    print(f"You have {rest_money:.2f} leva left!")
else:
    needed_money = total_price - budget
    print(f"Not enough money! You need {needed_money:.2f} leva more!")
