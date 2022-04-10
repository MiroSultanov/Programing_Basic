# Write a program that prints numbers in the range 1 to 1000 that end in 7.

for num in range(1, 1001):
    if num % 10 == 7:
        print(num)
