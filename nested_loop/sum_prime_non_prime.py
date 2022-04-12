# Write a program that reads integers from the console until a "stop" command is received. Find the sum of all entered primes and the sum of all
# entered primes. Since, by definition in mathematics, negative numbers cannot be prime, if a negative number is input, the following message
# "Number is negative." In this case, the entered number is ignored and is not added to either of the two amounts, and the program continues its execution,
# waiting for the next number to be entered.
# At the output to print in two lines the two amounts found in the following format:
#  "Sum of all prime numbers is: {prime numbers sum}"
# ⦁ "Sum of all non prime numbers is: {nonprime numbers sum}"


sum_of_prime_numbers = 0
sum_of_non_prime_numbers = 0
command = input()
while command != 'stop':
    current_number = int(command)
    if current_number < 0:
        print("Number is negative.")
    else:
        number_is_prime = True
        for number in range(2, current_number):
            if current_number % number == 0:
                number_is_prime = False
                break
        if number_is_prime:
            sum_of_prime_numbers += current_number
        else:
            sum_of_non_prime_numbers += current_number
    command = input()
print(f"Sum of all prime numbers is: {sum_of_prime_numbers}")
print(f"Sum of all non prime numbers is: {sum_of_non_prime_numbers}")
