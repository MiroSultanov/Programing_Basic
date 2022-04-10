# N integers are given in the interval [1… 1000]. Of these, some percentage p1 are below 200, another percentage p2 are from 200 to 399, another percentage
# p3 are from 400 to 599, another percentage p4 are from 600 to 799 and the remaining p5 percent are from 800 up. 
# Write a program that calculates and prints the percentages p1, p2, p3, p4 and p5.

count_of_numbers = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for num in range(count_of_numbers):
    current_number = int(input())
    if current_number < 200:
        p1 += 1
    elif current_number < 400:
        p2 += 1
    elif current_number < 600:
        p3 += 1
    elif current_number < 800:
        p4 += 1
    else:
        p5 += 1
print(f"{p1 / count_of_numbers * 100:.2f}%")
print(f"{p2 / count_of_numbers * 100:.2f}%")
print(f"{p3 / count_of_numbers * 100:.2f}%")
print(f"{p4 / count_of_numbers * 100:.2f}%")
print(f"{p5 / count_of_numbers * 100:.2f}%")
