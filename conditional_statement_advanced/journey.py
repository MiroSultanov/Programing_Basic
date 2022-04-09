budget = float(input())
season = input()
destination = " "
type_of_location = " "
total_price = 0
if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        total_price = budget * 0.30
        type_of_location = 'Camp'
    elif season == 'winter':
        total_price = budget * 0.70
        type_of_location = 'Hotel'
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        total_price = budget * 0.40
        type_of_location = 'Camp'
    elif season == 'winter':
        total_price = budget * 0.80
        type_of_location = 'Hotel'
else:
    destination = 'Europe'
    total_price = budget * 0.9
    type_of_location = 'Hotel'
print(f"Somewhere in {destination}")
print(f"{type_of_location} - {total_price:.2f}")