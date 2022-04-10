# Write a program that reads text (string) entered by the user and calculates and prints the sum of the values of the vowels according to the table below:
# letter a e i o u
# value  1 2 3 4 5

text = (input())
total_sum = 0
for av in (text):
    if av == "a":
        total_sum += 1
    if av == "e":
        total_sum += 2
    if av == "i":
        total_sum += 3
    if av == "o":
        total_sum += 4
    if av == "u":
        total_sum += 5
print(total_sum)
