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