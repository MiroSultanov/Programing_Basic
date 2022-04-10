# Write a program that reads the number n entered by the user and prints the numbers from 1 to n through 3.

number = int(input())
for num in range(1, number + 1, 3):
    print(num)
