# Write a program that reads an integer N entered by the user and generates all possible "special" numbers from 1111 to 9999. 
# To be a "special" number, it must meet the following condition:
# ⦁ N to be divisible by each of its digits without remainder.
# Example: at N = 16, 2418 is a special number:
# ⦁ 16/2 = 8 without residue
# ⦁ 16/4 = 4 without residue
# ⦁ 16/1 = 16 without residue
# ⦁ 16/8 = 2 without residue

# Input
# The input is read from the console and consists of an integer in the range [1… 600000]

# Output
# All "special" numbers must be printed on the console, separated by a space

number = int(input())
for current_number in range(1111, 10000):
    number_is_special = True
    current_number_as_string = str(current_number)
    for current_digit in current_number_as_string:
        if int(current_digit) == 0 or number % int(current_digit) != 0:
            number_is_special = False
            break
    if number_is_special:
        print(current_number, end=" ")
