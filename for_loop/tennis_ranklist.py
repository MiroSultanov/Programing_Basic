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