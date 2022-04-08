# Three athletes finish in a matter of seconds (between 1 and 50). Write a program that reads the times of the competitors in seconds entered by the user and calculates
# their total time in the format "minutes: seconds". Display seconds with leading zero (2 "02", 7 "07", 35 "35").

first_time = int(input())
second_time = int(input())
third_time = int(input())
total_time = first_time + second_time +third_time
minutes = total_time // 60
seconds = total_time - minutes * 60
if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")
