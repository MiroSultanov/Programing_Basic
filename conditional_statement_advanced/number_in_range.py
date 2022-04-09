# Write a program that checks whether the number entered by the user is in the range [-100, 100] and is different from 0 and displays "Yes" 
# if it meets the conditions, or "No" if it is outside them.

# Sample input and output

#       -25        Yes
#        0         No 
#        25        Yes

number = int(input())
if -100 <= number <= 100 and number != 0:
    print('Yes')
else:
    print('No')
