# In a movie theater, the chairs are arranged in a rectangular shape in r rows and c columns. There are three types of screenings with tickets at different prices:
# ⦁ Premiere - premiere screening, at a price of BGN 12.00;
# ⦁ Normal - standard screening, at a price of BGN 7.50;
# ⦁ Discount - screening for children, pupils and students at a reduced price of BGN 5.00.
# Write a program that reads the type of projection (text), the number of rows and the number of columns in the hall (integers) entered by the user,
# and calculates the total ticket revenue for a full hall. The result should be printed in 2 characters after the decimal point.

# Input          Output
# Premiere
# 10
# 12	            1440.00 leva	 	

# Normal
# 21
# 13	             2047.50 leva	

# Discount
# 12
# 30	             1800.00 leva


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

