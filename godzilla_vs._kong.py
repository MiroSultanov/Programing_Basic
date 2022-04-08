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