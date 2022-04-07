number_of_pages = int(input())
pages = int(input())
number_of_days = int(input())

total_time = number_of_pages // pages
hours_per_day = total_time // number_of_days

print(hours_per_day)