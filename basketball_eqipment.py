# Jesse decides he wants to play basketball, but he needs equipment to train. Write a program that Jesse will have to spend if you start training, knowing how much the basketball training fee is for a period of 1 year. Required equipment:
# ⦁ Basketball sneakers - their price is 40% less than the fee for one year
# ⦁ Basketball team - its price is 20% cheaper than that of sneakers
# ⦁ Basketball - price is 1/4 of the price of the basketball team
# ⦁ Basketball accessories - their price is 1/5 of the price of a basketball
# Entrance
# 1 line is read from the console:
# ⦁ The annual fee for basketball training - the whole number in the interval [0… 9999]
# Exit
# Print the console how much Jesse will be measured if he starts playing basketball.


annual_tax = int(input())
sneakers = annual_tax - (annual_tax * 0.4)
dress = sneakers - (sneakers * 0.2)
ball = dress / 4
accessories = ball / 5

total_sum_needed = annual_tax + sneakers + dress + ball + accessories
print(total_sum_needed)
