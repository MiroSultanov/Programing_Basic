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