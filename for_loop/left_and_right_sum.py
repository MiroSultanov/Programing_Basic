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