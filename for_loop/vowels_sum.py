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