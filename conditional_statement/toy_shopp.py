# Petya has a toy store. She receives a large order that she must fulfill. With the money he will earn he wants to go on a trip.
# Toy prices:
# ⦁ Puzzle - BGN 2.60.
# ⦁ Talking doll - BGN 3
# ⦁ Teddy bear - BGN 4.10
# ⦁ Minion - BGN 8.20
# ⦁ Truck - BGN 2
# If the ordered toys are 50 or more, the store makes a 25% discount on the total price. Petya has to give 10% of the earned money for the rent of the store. 
# To calculate whether the money will be enough for her to go on a trip.

vacation_price = float(input())
number_puzzles = int(input())
number_dolls = int(input())
number_bears = int(input())
number_minions = int(input())
number_trucks = int(input())

puzzle = 2.60
talking_doll = 3
teddy_bear = 4.10
minion = 8.20
truck = 2

price = puzzle * number_puzzles + talking_doll * number_dolls + teddy_bear * number_bears + minion * number_minions + \
        truck * number_trucks

toys_number = number_dolls + number_trucks + number_bears + number_minions + number_puzzles

if toys_number >= 50:
    discount = price * 0.25
else:
    discount = 0

total_sum = price - discount
rent = total_sum * 0.1
profit = total_sum - rent

if profit < vacation_price:
    needed_sum = vacation_price - profit
    print(f'Not enough money! {needed_sum:.2f} lv needed.')

else:
    left_sum = profit - vacation_price
    print(f'Yes! {left_sum:.2f} lv left.')
