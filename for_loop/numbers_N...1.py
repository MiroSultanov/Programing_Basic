# Write a program that reads a positive integer n entered by the user and prints the numbers n to 1 in reverse order. The number n entered will always be greater than 1.

number = int(input())
for num in range(number, 0, - 1):
    print(num)
