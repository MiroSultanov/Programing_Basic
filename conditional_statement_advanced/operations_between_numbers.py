# Write a program that reads two integers (N1 and N2) and an operator to perform a mathematical operation. 
# Possible operations are: Addition (+), Subtraction (-), Multiplication (*), Division (/) and Modular Division (%). 
# When adding, subtracting and multiplying the console, the result must be printed and whether it is even or odd. 
# In ordinary division - the result. In modular division - the remainder. It should be borne in mind that the divisor can be equal to 0 (zero) 
# and not divisible by zero. In this case, a special message must be printed.

# Entrance
# 3 lines entered by the user are read from the console:
# ⦁ N1 - integer;
# ⦁ N2 - integer;
# ⦁ Operator - one character between: "+", "-", "*", "/", "%".

# Exit
# Print one line on the console:
# ⦁ If the operation is addition, subtraction or multiplication:
# } "{N1} {operator} {N2} = {result} - {even / odd}"
# ⦁ If the operation is a division:
# ⦁ "{N1} / {N2} = {result}" - result formatted to the second decimal place
# ⦁ If the operation is a modular division:
# ⦁ "{N1}% {N2} = {remainder}"
# ⦁ In case of division by 0 (zero):
# ⦁ "Cannot divide {N1} by zero"

# Input
# 10
# 12
# +

N1 = int(input())
N2 = int(input())
symbol = input()
result = 0
even_odd = 0
if symbol in "+ - *":
    if symbol == "+":
        result = N1 + N2
        if result % 2 == 0:
            even_odd = "even"
        else:
            even_odd = "odd"
    elif symbol == "-":
        result = N1 - N2
        if result % 2 == 0:
            even_odd = "even"
        else:
            even_odd = "odd"
    elif symbol == "*":
        result = N1 * N2
        if result % 2 == 0:
            even_odd = "even"
        else:
            even_odd = "odd"
    print(f"{N1} {symbol} {N2} = {result} - {even_odd}")
elif symbol == "/":
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        result = N1 / N2
        print(f"{N1} / {N2} = {result:.2f}")
elif symbol == "%":
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        result = N1 % N2
        print(f"{N1} % {N2} = {result}")
