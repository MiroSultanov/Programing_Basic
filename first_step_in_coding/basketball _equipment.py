annual_tax = int(input())
sneakers = annual_tax - (annual_tax * 0.4)
dress = sneakers - (sneakers * 0.2)
ball = dress / 4
accessories = ball / 5

total_sum_needed = annual_tax + sneakers + dress + ball + accessories
print(total_sum_needed)