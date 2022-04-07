# There are a number of books on Joro's list of required literature for the summer holidays. Because Joro prefers to play with friends outside, 
# your task is to help him calculate how many hours a day he has to spend reading the necessary literature.

# Entrance
# 3 lines are read from the console:
# Number of pages in the current book - integer in the interval [1… 1000]
# Pages read in 1 hour - integer in the interval [1… 1000]
# The number of days for which you must read the book - an integer in the range [1… 1000]

# Exit
# To print on the console the number of hours that Joro has to read each day.

number_of_pages = int(input())
pages = int(input())
number_of_days = int(input())

total_time = number_of_pages // pages
hours_per_day = total_time // number_of_days

print(hours_per_day)
