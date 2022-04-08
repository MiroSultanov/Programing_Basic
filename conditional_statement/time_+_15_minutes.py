# Write a program that reads the hour and minutes of the 24-hour day entered by the user and calculates what time it will be in 15 minutes. 
# Print the result in hours: minutes format. The hours are always between 0 and 23, and the minutes are always between 0 and 59. 
# The hours are written in one or two digits. Minutes are always displayed in two digits, with a leading zero when necessary.

hour = int(input())
minutes = int(input())
minutes += 15
hour += minutes // 60
minutes = minutes % 60
if hour > 23:
    hour = 0
if minutes <= 9:
    print(f"{hour}:0{minutes}")
else:
    print(f"{hour}:{minutes}")
