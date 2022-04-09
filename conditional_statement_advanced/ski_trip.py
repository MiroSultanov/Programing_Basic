# Atanas decided to spend his vacation in Bansko and ski. Before leaving, however, he must book a hotel and calculate how much his stay will cost. The following types of accommodation are available, with the following accommodation prices:
# ⦁ "room for one person" - BGN 18.00 per night
# ⦁ "apartment" - BGN 25.00 per night
# ⦁ "president apartment" - BGN 35.00 per night
# Depending on the number of days he will stay in the hotel (example: 11 days = 10 nights) and the type of room he chooses, he can enjoy different discounts.

# room type               less than 10 days            between 10 and 15 days            more than 15 days
# room for one person    does not use a reduction      does not use a reduction         does not use a reduction
# apartment              30% of the final price        35% of the final price            50% of the final price
# president apartment    10% of the final price        15% of the final price            20% of the final price

# After the stay, Atanas' rating for the hotel's services can be positive or negative. If his assessment is positive, Atanas adds 25% of it to the price with the already deducted discount. If his assessment is negative, 10% is deducted from the price.
# Entrance
# The input is readable from the console and consists of three lines:
# ⦁ First row - days of stay - integer in the interval [0 ... 365]
# ⦁ Second row - room type - "room for one person", "apartment" or "president apartment"
# ⦁ Third line - evaluation - "positive" or "negative"
# Exit
# One line must be printed on the console:
# ⦁ The price for his stay at the hotel, formatted to the second decimal place.

# Input
# 14
# apartment
# positive

days_for_stay = int(input())
type_of_room = input()
grade = input()
price_for_stay = 0
room_for_one_person = 18
apartment = 25
president_apartment = 35
nights = days_for_stay - 1
if type_of_room == 'apartment':
    if days_for_stay <= 10:
        price_for_stay = (nights * apartment) * 0.70
    elif 10 < days_for_stay <= 15:
        price_for_stay = (nights * apartment) * 0.65
    elif days_for_stay > 15:
        price_for_stay = (nights * apartment) * 0.50
        if grade == 'positive':
            price_for_stay = price_for_stay * 0.75
        elif grade == 'negative':
            price_for_stay = price_for_stay * 0.90
elif type_of_room == 'president apartment':
    if days_for_stay <= 10:
        price_for_stay = (nights * president_apartment) * 0.90
    elif 10 < days_for_stay <= 15:
        price_for_stay = (nights * president_apartment) * 0.85
    elif days_for_stay > 15:
        price_for_stay = (nights * president_apartment) * 0.80
        if grade == 'positive':
            price_for_stay = price_for_stay * 0.75
        elif grade == 'negative':
            price_for_stay = price_for_stay * 0.90
elif type_of_room == 'room_for_one_person':
    if grade == 'positive':
        price_for_stay = price_for_stay * 0.75
    elif grade == 'negative':
        price_for_stay = price_for_stay * 0.90
print(f"{price_for_stay:.2f}")
