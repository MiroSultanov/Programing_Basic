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