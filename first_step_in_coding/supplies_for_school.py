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