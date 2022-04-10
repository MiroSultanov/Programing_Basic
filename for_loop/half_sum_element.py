# Write a program that reads n-number integers entered by the user and checks if there is a number among them that is equal to the sum of all the others.
# ⦁ If there is such an element, print "Yes" and on a new line "Sum =" + its value
# ⦁ If there is no such element, print "No" and on a new line "Diff =" + the difference between the largest element and the sum of the others (in absolute value)

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
