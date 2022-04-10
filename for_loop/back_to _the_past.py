inherited_money = float(input())
year_which_he_lives = int(input())
spend_money = 0
for current_year in range(1800, year_which_he_lives + 1):
    if current_year % 2 == 0:
        spend_money += 12000
    else:
        diff = abs(year_which_he_lives - current_year)
        spend_money += 12000 + 50 * (18 + diff)
difference = abs(inherited_money - spend_money)
if inherited_money >= spend_money:
    print(f"Yes! He will live a carefree life and will have {difference:.2f} dollars left.")
else:
    print(f"He will need {difference:.2f} dollars to survive.")