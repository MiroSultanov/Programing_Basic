# Grigor Dimitrov is a tennis player whose next goal is to rise in the world rankings in men's tennis.
# During the year Grisho participates in a number of tournaments, receiving points for each tournament, which depend on the position in which he 
# finished in the tournament. There are three options for completing a tournament:
# ⦁ W - if the winner receives 2000 points
# ⦁ F - if he is a finalist he receives 1200 points
# ⦁ SF - if he is a semifinalist he gets 720 points
# Write a program that calculates how many points Grigor will have after playing all the tournaments, knowing how many points the season starts with. 
# Also calculate how many points he averages on all tournaments played and what percentage of tournaments he has won.

# Entrance
# Two lines are read from the console first:
# ⦁ Number of tournaments in which he participated - integer in the interval [1… 20]
# ⦁ Initial number of points in the rankings - an integer in the range [1 ... 4000]
# A separate line is read for each tournament:
# ⦁ Reached the stage of the tournament - text - "W", "F" or "SF"

# Exit
# Three lines are printed in the following format:
# ⦁ "Final points: {number of points after tournaments played}"
# ⦁ "Average points: {average points earned per tournament}"
# ⦁ "{percentage of tournaments won}%"
# The middle points should be rounded down to the nearest whole number, and the percentage should be formatted to the second digit after the decimal point.

from math import floor

numbers_tournaments = int(input())
start_points = int(input())
percent = 0
numbers_win = 0
total_points = start_points

for i in range(numbers_tournaments):
    type_tournament = input()
    if type_tournament == 'W':
        total_points += 2000
        numbers_win += 1
    elif type_tournament == 'F':
        total_points += 1200
    elif type_tournament == 'SF':
        total_points += 720

print(f"Final points: {total_points}")
average_points = (total_points - start_points) / numbers_tournaments
print(f'Average points: {floor(average_points)}')
percent = numbers_win / numbers_tournaments * 100
print(f'{percent:.2f}%')
