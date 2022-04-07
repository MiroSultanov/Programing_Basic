square_meters_for_landscape = float(input())
price_for_the_whole_yard = square_meters_for_landscape * 7.61

discount = price_for_the_whole_yard * 0.18

total_sum = price_for_the_whole_yard - discount
print(f'f The final price is {total_sum}')
print(f'f The discount is {discount}')