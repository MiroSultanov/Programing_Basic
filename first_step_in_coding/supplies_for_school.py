# The school year has already started and the head of 10B class - Ani has to buy a certain number of packets of chemicals, 
# packets of markers and detergent for cleaning the board. She is a regular customer of a bookstore, so there is a discount for her, 
# which is a percentage of the total. Write a program that calculates how much money Annie will have to raise to pay the bill, keeping in mind the following price list:
# ⦁ Package of chemicals - BGN 5.80.
# ⦁ Package of markers - BGN 7.20.
# ⦁ Detergent - BGN 1.20 (per liter)

# Entrance
# 4 numbers are read from the console:
# Number of packages of chemicals - an integer in the range [0 ... 100]
# Number of packet markers - integer in the range [0 ... 100]
# Liters of board cleaner - integer in the range [0… 50]
# Percentage reduction - an integer in the range [0 ... 100]

# Exit
# Print on the console how much money Annie will need to pay her bill.

number_of_pens = int(input())
number_of_markers = int(input())
litter_of_detegrant = int(input())
percent_discount = int(input())

price_for_pack_of_pens = number_of_pens * 5.80
price_for_pack_of_markers = number_of_markers * 7.20
price_for_litter_of_detegrant = litter_of_detegrant * 1.20
total = price_for_pack_of_pens + price_for_pack_of_markers +price_for_litter_of_detegrant
discount = percent_discount / 100
price_with_discount = total - (total * discount)
print(price_with_discount)
