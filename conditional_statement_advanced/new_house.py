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