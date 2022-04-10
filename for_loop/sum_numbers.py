# Write a program that reads n-number integers entered by the user and sums them.
# ⦁ Enter the number of numbers n from the first line of the input.
# ⦁ Enter an integer from the next n lines.
# The program must read the numbers, sum them and print their sum.

number = int(input())
total_sum = 0

for _ in range(number):
    current_num = int(input())
    total_sum += current_num

print(total_sum)
