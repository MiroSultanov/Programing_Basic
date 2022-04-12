# Write a program that reads two six-digit integers from the console. The first number entered will always be less than the second. 
# On the console to be printed on 1, line separated by a space, all numbers that are between the two numbers read by the console and meet the condition
# that the sum of the digits of even and odd positions are equal. 
# If there are no numbers that meet the console condition, no result is displayed.

first_number = int(input())
second_number = int(input())
for current_number in range(first_number, second_number + 1):
    odd_digit_sum = 0
    even_digit_sum = 0
    current_number_as_string = str(current_number)
    for index, digit in enumerate(current_number_as_string):
        if index % 2 == 0:
            odd_digit_sum += int(digit)
        else:
            even_digit_sum += int(digit)
    if odd_digit_sum == even_digit_sum:
        print(current_number_as_string, end=" ")
