# Write a program that, before receiving the "Stop" command, reads integers entered by the user, finds at least one of them and prints it. Enter one number per line.

import sys

max_number = sys.maxsize
while True:
    numbers = input()
    if numbers == "Stop":
        break
    elif int(numbers) < max_number:
        max_number = int(numbers)
print(max_number)
