# The company gives the following commissions to its merchants according to the city in which they work and the volume of sales:
    
# city	0 ≤ s ≤ 500  	500 < s ≤ 1 000 	1 000 < s ≤ 10 000  	s > 10 000
# Sofia	  5%	              7%	              8%	                12%
# Varna	4.5%	             7.5%	              10%	                13%
# Plovdiv	5.5%	          8%	              12%	                14.5%

# Write a console program that reads the city name (text) and sales volume (real number) entered by the user, and calculates and displays the amount of the trade 
# commission according to the table above. Display the result formatted to 2 digits after the decimal point. 
# In case of invalid city or sales volume (negative number) print "error".


city = input()
sales_volume = float(input())
commissions = 0
conditional = True
if city == 'Sofia':
    if 0 <= sales_volume <= 500:
        commissions = sales_volume * 0.05
    elif 500 < sales_volume <= 1000:
        commissions = sales_volume * 0.07
    elif 1000 < sales_volume <= 10000:
        commissions = sales_volume * 0.08
    elif sales_volume > 10000:
        commissions = sales_volume * 0.12
    else:
        conditional = False

elif city == 'Varna':
    if 0 <= sales_volume <= 500:
        commissions = sales_volume * 0.045
    elif 500 < sales_volume <= 1000:
        commissions = sales_volume * 0.075
    elif 1000 < sales_volume <= 10000:
        commissions = sales_volume * 0.10
    elif sales_volume > 10000:
        commissions = sales_volume * 0.13
    else:
        conditional = False

elif city == 'Plovdiv':
    if 0 <= sales_volume <= 500:
        commissions = sales_volume * 0.055
    elif 500 < sales_volume <= 1000:
        commissions = sales_volume * 0.08
    elif 1000 < sales_volume <= 10000:
        commissions = sales_volume * 0.12
    elif sales_volume > 10000:
        commissions = sales_volume * 0.145
    else:
        conditional = False
else:
    conditional = False

if conditional:
    print(f'{commissions:.2f}')
else:
    print('error')
