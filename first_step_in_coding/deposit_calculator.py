deposit = float(input())
month = int(input())
annual_interest_percent = float(input())
annual_interest = deposit * annual_interest_percent / 100
month_interest = annual_interest / 12
total_sum = deposit + (month * month_interest)
print(total_sum)