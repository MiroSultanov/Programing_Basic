# Rumen wants to repaint the living room and has hired craftsmen for this purpose. Write a program that calculates the cost of repairs, given the following prices:
# ⦁ Protective nylon - BGN 1.50 per square meter
# ⦁ Paint - BGN 14.50 per liter
# Боя Paint thinner - BGN 5.00 per liter
# Just in case, to the necessary materials, Rumen wants to add another 10% of the amount of paint and 2 sq.m. nylon, of course BGN 0.40 for bags. 
# The amount paid to the masters for 1 hour of work is equal to 30% of the sum of all costs for materials.

# Entrance
# The input is readable from the console and contains exactly 4 lines:
# Required amount of nylon (in sq.m.) - an integer in the range [1 ... 100]
# Required amount of paint (in liters) - an integer in the range [1… 100]
# Diluent quantity (in liters) - integer in the range [1… 30]
# The hours for which the masters will do the work - an integer in the interval [1… 9]

# Exit
# Print one line on the console:
# "{sum of all expenses}"

squared_meter_of_nylon = int(input())
litters_of_paint = int(input())
litters_of_thinner = int(input())
working_hours = int(input())

sum_for_nylon = (squared_meter_of_nylon + 2) * 1.50
sum_for_paint = (litters_of_paint + (litters_of_paint * 0.1)) * 14.50
sum_for_thinner = litters_of_thinner * 5
sum_for_bags = 0.40
sum_for_materials = sum_for_nylon + sum_for_paint + sum_for_thinner + sum_for_bags
sum_for_working_hours = (sum_for_materials * 0.3) * working_hours
final_price_for_repainting = sum_for_materials + sum_for_working_hours
print(f"The final price for repainting is: {final_price_for_repainting} lv.")
