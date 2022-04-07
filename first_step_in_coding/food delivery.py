chicken_menu = int(input())
fish_menu = int(input())
vegan_menu = int(input())

price_for_chicken_menu = chicken_menu * 10.35
price_for_fish_menu = fish_menu * 12.40
price_for_vegan_menu = vegan_menu * 8.15
total_sum = price_for_chicken_menu + price_for_fish_menu + price_for_vegan_menu
price_for_desert = 0.2 * total_sum
delivery = 2.50
total_sum_order = total_sum + price_for_desert + delivery
print(f"{total_sum_order:.2f}")