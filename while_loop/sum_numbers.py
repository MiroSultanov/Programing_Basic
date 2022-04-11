# Write a program that reads an integer from the console and integers on each line until their sum is greater than or equal to the original number. 
# At the end of the reading, print the sum of the entered numbers.

number = int(input())
sum_numbers = 0
while sum_numbers < number:
    current_number = int(input())
    sum_numbers += current_number
print(sum_numbers)
