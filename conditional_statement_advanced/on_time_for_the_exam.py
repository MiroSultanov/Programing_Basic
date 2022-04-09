# A student must go to the exam at a certain time (for example, at 9:30). He comes to the examination hall at a certain time of arrival (for example 9:40).
# It is considered that the student arrived on time if he arrived at the time of the exam or up to half an hour before. 
# If he arrived more than 30 minutes earlier, he was early. If he came after the exam time, he was late. 
# Write a program that reads exam time and arrival time and records whether the student arrived on time, was early or late, and by how many hours or 
# minutes was early or late.

# Entrance
# The console reads 4 integers (one per line) entered by the user:
# ⦁ The first line contains the exam time - an integer from 0 to 23;
# ⦁ The second line contains a minute of the exam - an integer from 0 to 59;
# ⦁ The third line contains the time of arrival - an integer from 0 to 23;
# ⦁ The fourth line contains the minute of arrival - an integer from 0 to 59.

# Exit
# On the first line print:
# ⦁ "Late" if the student arrives later than the exam time;
# ⦁ "On time", if the student arrives exactly at the time of the exam or up to 30 minutes earlier;
# "" Early "if the student arrives more than 30 minutes before the exam time.
# If the student arrives at least one minute apart from the exam time, print on the following line:
# ⦁ "mm minutes before the start" for arriving earlier by less than an hour;
# "" Hh: mm hours before the start "for 1 hour or more early. Always print the minutes in 2 digits, for example "1:05";
# "" Mm minutes after the start "for a delay of less than an hour;
# "" Hh: mm hours after the start "for a delay of 1 hour or more. Always print the minutes with 2 digits, for example "1:03".
        
# Input
# 9
# 30
# 9
# 50

hour_of_examine = int(input())
minute_of_examine = int(input())
hour_of_arriving = int(input())
minutes_of_arriving = int(input())
time_of_examine = hour_of_examine * 60 + minute_of_examine
time_of_arriving = hour_of_arriving * 60 + minutes_of_arriving
if time_of_arriving > time_of_examine:
    print('Late')
elif time_of_examine - 30 <= time_of_arriving <= time_of_examine:
    print('On time')
else:
    print('Early')
difference = abs(time_of_arriving - time_of_examine)
if time_of_examine - 60 < time_of_arriving < time_of_examine:
    print(f"{difference} minutes before the start")
elif time_of_arriving <= time_of_examine - 60:
    hours = difference // 60
    minutes = difference % 60
    if minutes < 10:
        print(f"{hours}:0{minutes} hours before the start")
    else:
        print(f"{hours}:{minutes} hours before the start")
elif time_of_examine < time_of_arriving < time_of_examine + 60:
    print(f"{difference} minutes after the start")
elif time_of_arriving >= time_of_examine + 60:
    hours = difference // 60
    minutes = difference % 60
    if minutes < 10:
        print(f"{hours}:0{minutes} hours after the start")
    else:
        print(f"{hours}:{minutes} hours after the start")
