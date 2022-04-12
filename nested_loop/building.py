# Write a program that displays the numbers of the rooms in a building (in descending order) on the console, provided that the following conditions are met:
# ⦁ There are only offices on each even floor;
# ⦁ There are only apartments on each odd floor;
# ⦁ Each apartment is denoted as follows: A {floor number} {apartment number}, apartment numbers start from 0;
# ⦁ Each office is denoted as follows: О {floor number} {office number}, office numbers also start from 0;
# ⦁ There are always apartments on the top floor and they are bigger than the others, so their number says 'L' instead of 'A'. 
# If there is only one floor, there are only large apartments!
# Two integers are read from the console - the number of floors and the number of rooms per floor.

number_of_floors = int(input())
number_of_rooms = int(input())
rooms_numbers = ' '
for f in range(number_of_floors, 0, -1):
    for r in range(number_of_rooms):
        current_number_of_room = f * 10 + r
        if f == number_of_floors:
            print(f'L{current_number_of_room} ', end='')
        elif f % 2 != 0:
            rooms_numbers += f'A{current_number_of_room} '
        else:
            rooms_numbers += f'O{current_number_of_room} '
    print(rooms_numbers)
    rooms_numbers = ' '
