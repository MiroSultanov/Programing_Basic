# During the lunch break you want to watch an episode of your favorite series. 
# Your task is to write a program that will find out if you have enough time to watch the episode. 
# During the holiday you spend time for lunch and time for rest. Lunch time will be 1/8 of the rest time, and rest time will be 1/4 of the rest time.

# Entrance
# 3 lines are read from the console:
# ⦁ Name of the series - text
# ⦁ Episode duration - integer in the range [10… 90]
# ⦁ Duration of the break - an integer in the range [10… 120]

# Exit
# Write one line on the console:
# ⦁ If you have enough time to watch the episode:
# "You have enough time to watch {series name} and left with {free time} minutes free time."
# ⦁ If you do not have enough time:
# "You don't have enough time to watch {series name}, you need {time} more minutes."
# Time to round to the nearest whole number up.

import math
name_of_series = input()
duration_of_episode = int(input())
duration_of_break = int(input())
time_for_lunch = duration_of_break * (1/8)
time_for_relax = duration_of_break * (1/4)
total_time = duration_of_episode + time_for_relax + time_for_lunch
if duration_of_break >= total_time:
    time_left = duration_of_break - total_time
    print(f"You have enough time to watch {name_of_series} and left with {math.ceil(time_left)} minutes free time.")
elif duration_of_break < total_time:
    time_needed = total_time - duration_of_break
    print(f"You don't have enough time to watch {name_of_series}, you need {math.ceil(time_needed)} more minutes.")
