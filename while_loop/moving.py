On his eighteenth birthday, Jose decided to move out. He packed his luggage in boxes and found a suitable advertisement for an apartment for rent. 
He begins to carry his luggage in parts because he can't at once. He has limited free space in his new home, where he can place his belongings so that the place is 
suitable for living.
# Write a program that calculates the free volume of Jose's home that remains after moving your luggage.
# Each box has the exact dimensions: 1m x 1m x 1m.

# Input
# The user enters the following data on separate lines:
# ⦁ Width of free space - integer;
# ⦁ Length of free space - integer;
# ⦁ Height of free space - integer;
# ⦁ On the following lines (until receiving the command "Done") - number of boxes to be transferred to the accommodation - integers
# The program should finish reading data at the "Done" command or if the free space runs out.

# Output
# Print one of the following lines on the console:
# ⦁ If you reach the "Done" command and there is still free space:
# "{number of free cubic meters left} Cubic meters left."
# ⦁ If the free space runs out before the "Done" command arrives:
# "No more free space! You need {number of missing cubic meters} Cubic meters more."

width = int(input())
length = int(input())
height = int(input())
total_volume = width * length * height
is_there_more_free_space = True
command = input()
while command != "Done":
    number_of_boxes = int(command)
    total_volume -= number_of_boxes
    if total_volume < 0:
        is_there_more_free_space = False
        break
    command = input()
if is_there_more_free_space:
    print(f"{total_volume} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(total_volume)} Cubic meters more.")
