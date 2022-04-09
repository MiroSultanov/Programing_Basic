# The hotel offers 2 types of rooms: studio and apartment. Write a program that calculates the price for the entire stay for a studio and apartment. 
# Prices depend on the month of stay:
    
# May and October              June and September            July and August
# Studio - BGN 50/night       Studio - BGN 75.20/night      Studio - BGN 76 / night
# Apartment - 65 BGN/night   Apartment - 68.70 BGN/night    Apartment - 77 BGN / night 

# The following discounts are also available:
# ⦁ For studio, for more than 7 nights in May and October: 5% discount.
# ⦁ For studio, for more than 14 nights in May and October: 30% discount.
# ⦁ For studio, for more than 14 nights in June and September: 20% discount.
# ⦁ For an apartment, for more than 14 nights, regardless of the month: 10% discount.
# Entrance
# The input is readable by the console and contains exactly 2 lines entered by the user:
# ⦁ On the first row is the month - May, June, July, August, September or October;
# ⦁ On the second row is the number of nights - an integer.
# Exit
# To print 2 lines on the console:
# ⦁ In the first line: "Apartment: {price for the whole stay} lv."
# ⦁ On the second line: "Studio: {price for the whole stay} lv."
# The price for the entire stay must be formatted to two decimal places.

# Input
# May    
# 15

month = input()
nights = int(input())
studio_price = 0
apartment_price = 0

if month == 'May' or month == 'October':
    studio_price = 50 * nights
    apartment_price = 65 * nights
    if 7 < nights <= 14:
        studio_price = studio_price - (studio_price * 0.05)
    elif nights > 14:
        studio_price = studio_price - (studio_price * 0.3)
elif month == 'June' or month == 'September':
    studio_price = 75.20 * nights
    apartment_price = 68.70 * nights
    if nights > 14:
        studio_price = studio_price - (studio_price * 0.2)
elif month == 'July' or month == 'August':
    studio_price = 76 * nights
    apartment_price = 77 * nights

if nights > 14:
    apartment_price = apartment_price - (apartment_price * 0.1)

print(f'Apartment: {apartment_price:.2f} lv.')
print(f'Studio: {studio_price:.2f} lv.')
