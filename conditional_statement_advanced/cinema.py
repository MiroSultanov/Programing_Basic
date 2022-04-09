screening_type = input()
number_of_rows = int(input())
number_of_column = int(input())
income = 0
total_places = number_of_column * number_of_rows
if screening_type == 'Premiere':
    income = total_places * 12.00
elif screening_type == 'Normal':
    income = total_places * 7.50
elif screening_type == 'Discount':
    income = total_places * 5.00
print(f"{income:.2f} leva")

