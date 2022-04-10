# Write a program that reads 2 * n numbers of integers submitted by the user and checks if the sum of the first n numbers (left sum) is equal 
# to the sum of the second n numbers (right sum). In case of equality, print "Yes, sum =" + the amount; otherwise print "No, diff =" + the difference. 
# The difference is calculated as a positive number (in absolute value).

number = int(input())
left_sum = 0
right_sum = 0
for num in range(0, number):
    current_number = int(input())
    left_sum = left_sum + current_number
for num in range(0, number):
    current_number = int(input())
    right_sum = right_sum + current_number

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    difference = abs(left_sum - right_sum)
    print(f"No, diff = {difference}")
