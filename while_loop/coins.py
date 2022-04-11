# Vending machine manufacturers wanted to make their machines return as few change coins as possible. 
# Write a program that accepts an amount - the rest that needs to be returned and calculates with as few coins as possible.

sum = float(input())
sum = int(sum * 100)
coins_counter = 0
coins_counter += sum // 200
sum = sum % 200
coins_counter += sum // 100
sum = sum % 100
coins_counter += sum // 50
sum = sum % 50
coins_counter += sum // 20
sum = sum % 20
coins_counter += sum // 10
sum = sum  % 10
coins_counter += sum // 5
sum = sum % 5
coins_counter += sum // 2
sum = sum  % 2
coins_counter += sum // 1
sum = sum % 1
print(coins_counter)
