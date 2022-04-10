import sys

count_of_number = int(input())
max_number = -sys.maxsize
sum_numbers = 0
for num in range(count_of_number):
    current_number = int(input())
    sum_numbers += current_number
    if current_number > max_number:
        max_number = current_number
if max_number == sum_numbers - max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    difference = abs(max_number - (sum_numbers - max_number))
    print("No")
    print(f"Diff = {difference}")
