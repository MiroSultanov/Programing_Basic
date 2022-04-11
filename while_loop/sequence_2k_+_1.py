# Write a program that reads the number n entered by the user and prints all the numbers ≤ n from the sequence: 1, 3, 7, 15, 31,…. 
# Each subsequent number is calculated by multiplying the previous one by 2 and adding 1.

number = int(input())
counter = 1
while counter <= number:
    print(counter)
    counter += counter + 1
