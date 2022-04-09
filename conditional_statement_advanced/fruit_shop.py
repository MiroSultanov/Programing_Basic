# Write a program that reads from the console the following three variables entered by the user and calculates the price according to the prices in the tables above:
# ⦁ fruit - banana / apple / orange / grapefruit / kiwi / pineapple / grapes;
# ⦁ day of the week - Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Sunday;
# ⦁ quantity (real number).
# Print the result rounded with 2 digits after the decimal point. In case of invalid day of the week or invalid fruit name, print "error".

# Fruit shop on weekdays works at the following prices:
# fruit	banana	apple	orange	grapefruit	kiwi	pineapple	grapes
# price	2.50	1.20	0.85	1.45	        2.70	 5.50	         3.85

# On Saturdays and Sundays the store is open at higher prices:
# fruit	banana	apple	orange	grapefruit	kiwi	pineapple	grapes
# price	2.70	1.25	0.90	 1.60	         3.00	 5.60	         4.20

        
        
fruit = input()
day_of_week = input()
quantity = float(input())
price = 0

if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday' \
        or day_of_week == 'Friday':
    if fruit == 'banana':
        price = 2.50
    elif fruit == 'apple':
        price = 1.20
    elif fruit == 'orange':
        price = 0.85
    elif fruit == 'grapefruit':
        price = 1.45
    elif fruit == 'kiwi':
        price = 2.70
    elif fruit == 'pineapple':
        price = 5.50
    elif fruit == 'grapes':
        price = 3.85

elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
    if fruit == 'banana':
        price = 2.70
    elif fruit == 'apple':
        price = 1.25
    elif fruit == 'orange':
        price = 0.90
    elif fruit == 'grapefruit':
        price = 1.60
    elif fruit == 'kiwi':
        price = 3.00
    elif fruit == 'pineapple':
        price = 5.60
    elif fruit == 'grapes':
        price = 4.20

if price == 0:
    print('error')
else:
    total_sum = quantity * price
    print(f'{total_sum:.2f}')
