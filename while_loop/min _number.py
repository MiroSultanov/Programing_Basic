import sys

max_number = sys.maxsize
while True:
    numbers = input()
    if numbers == "Stop":
        break
    elif int(numbers) < max_number:
        max_number = int(numbers)
print(max_number)