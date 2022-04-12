# Write a program that checks all possible combinations of a pair of numbers in the interval of two given numbers. 
# The output is printed, which is the combination whose sum of numbers is equal to a given magic number.
# If there is no combination that matches the condition, a message is printed that it was not found.

# Input
# The input is readable from the console and consists of three lines:
# ⦁ First line - beginning of the interval - integer in the interval [1 ... 999]
# ⦁ Second line - end of the interval - integer in the interval [greater than the first number ... 1000]
# ⦁ Third row - the magic number - an integer in the interval [1 ... 10000]

# Output
# One line should be printed on the console, according to the result:
# ⦁ If a combination is found whose sum of numbers is equal to the magic number
# ⦁ "Combination N: {sequence number} ({first number} + {second number} = {magic number})"
# ⦁ If no matching condition is found
# } "{Number of all combinations} combinations - neither equals {magic number}"

starting_interval = int(input())
final_interval = int(input())
magic_number = int(input())
combination = 0
condition = False
for i in range(starting_interval, final_interval + 1):
    for x in range(starting_interval, final_interval + 1):
        combination += 1
        if i + x == magic_number:
            condition = True
            print(f"Combination N:{combination} ({i} + {x} = {magic_number})")
            break

    if condition:
        break

if not condition:
    print(f"{combination} combinations - neither equals {magic_number}")
