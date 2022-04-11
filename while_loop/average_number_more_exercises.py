number = int(input())
sum = 0
average_number = 0
for number in range(number):
    sum = sum + number
    average_number = sum / number
print(f"{average_number:.2f}")