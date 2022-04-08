# An integer is given - the starting number of points. Bonus points are accrued on it according to the rules described below. 
# Write a program that calculates the bonus points received by the number and the total number of points (number + bonus).
# ⦁ If the number is up to 100 inclusive, the bonus points are 5;
# ⦁ If the number is greater than 100, the bonus points are 20% of the number;
# ⦁ If the number is greater than 1000, the bonus points are 10% of the number.

# ⦁ Additional bonus points (accrued separately from the previous ones):
# ⦁ For an even number + 1 point.
# ⦁ For a number ending in 5 + 2 points.

number = int(input())
bonus_point = 0
if number <= 100:
    bonus_point += 5
elif 100 < number <= 1000:
    bonus_point += number * 0.2
else:
    bonus_point += number * 0.1
if number % 2 == 0:
    bonus_point += 1
if number % 10 == 5:
    bonus_point += 2
print(bonus_point)
print(number + bonus_point)
