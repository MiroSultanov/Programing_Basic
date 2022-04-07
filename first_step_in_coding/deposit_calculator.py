# Write a program that calculates how much you will receive at the end of the deposit period at a certain interest rate. Use the following formula:
# amount = deposited amount + term of the deposit * (deposited amount * annual interest rate) / 12)

# Entrance
# 3 lines are read from the console:
# Deposit amount - real number in the interval [100.00… 10000.00]
# Deposit term (in months) - integer in the interval [1… 12]
# Annual interest rate - real number in the interval [0.00… 100.00]

# Exit
# Print the amount on the console at the end of the term.

deposit = float(input())
month = int(input())
annual_interest_percent = float(input())
annual_interest = deposit * annual_interest_percent / 100
month_interest = annual_interest / 12
total_sum = deposit + (month * month_interest)
print(total_sum)
