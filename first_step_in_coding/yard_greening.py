# Bozhidara has several houses on the Black Sea coast and wants to green the yards of some of them, thus creating a cozy atmosphere and comfort for its guests. 
# She has hired a company for this purpose.
# Write a program that calculates the amount needed that Bozhidara will have to pay to the project contractor. 
# The price per square meter is BGN 7.61 with VAT. Because her yard is quite large, the contractor company offers an 18% discount on the final price.

# Entrance
# Only one line is read from the console:
# ⦁ Sq. meters to be landscaped - real number in the range [0.00… 10000.00]

# Exit
# Two lines are printed on the console:
# "The final price is: {final price of the service} lv."
# "The discount is: {discount} lv."

square_meters_for_landscape = float(input())
price_for_the_whole_yard = square_meters_for_landscape * 7.61

discount = price_for_the_whole_yard * 0.18

total_sum = price_for_the_whole_yard - discount
print(f'f The final price is {total_sum}')
print(f'f The discount is {discount}')
