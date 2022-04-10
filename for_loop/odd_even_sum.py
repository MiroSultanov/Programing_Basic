# Write a program that reads n-number integers submitted by the user and checks that the sum of the numbers of even positions is equal to the sum of the numbers
# of odd positions.
# ⦁ If the amounts are equal, print two lines: "Yes" and on a new line "Sum =" + the amount;
# ⦁ If the amounts are not equal, print two lines: "No" and a new line "Diff =" + the difference.
# The difference is calculated in absolute value.

number = int(input())
even_sum = 0
odd_sum = 0
for num in range(number):
    current_number = int(input())
    if num % 2 == 0:
        even_sum += current_number
    else:
        odd_sum += current_number
if odd_sum == even_sum:
    print('Yes')
    print(f"Sum = {even_sum}")
else:
    diff = abs (odd_sum - even_sum)
    print('No')
    print(f"Diff = {diff}")
