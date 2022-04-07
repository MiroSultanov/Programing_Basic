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