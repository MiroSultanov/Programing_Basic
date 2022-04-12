# Print on the console the multiplication table for the numbers 1 to 10 in the format:
# "{first multiplier} * {second multiplier} = {result}".

for n1 in range(1, 11):
    for n2 in range(1,11):
        result = n1 * n2
        print(f"{n1} * {n2} = {result}")
