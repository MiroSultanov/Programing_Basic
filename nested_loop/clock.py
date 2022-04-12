# Write a program that prints the hours of the day from 0: 0 to 23:59, each on a separate line. The hours must be displayed in the format "{hour}: {minutes}".

for h in range(24):
    for m in range(60):
        print(f"{h}:{m}")
