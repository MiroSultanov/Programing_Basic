# Write a program that reads the number n entered by the user and prints the even degrees of 2 ≤ 2^n: 2^0, 2^2, 2^4, 2^6,…, 2^n.

number = int(input())
for num in range(number + 1):
    if num % 2 == 0:
        print(2 ** num)
