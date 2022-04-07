# For his birthday, Lubomir received an aquarium in the shape of a parallelepiped. Initially, we read from the console in separate rows its 
# dimensions - length, width and height in centimeters. It is necessary to calculate how many liters of water the aquarium will collect if it is known that a 
# certain percentage of its capacity is occupied by sand, plants, heater and pump.
# One liter of water is equal to one cubic decimeter / 1l = 1 dm3 /.
# Write a program that calculates the liters of water needed to fill the aquarium.

# Entrance
# 4 lines are read from the console:
# Length in cm - integer in the range [10… 500]
# Width in cm - integer in the range [10… 300]
# Height in cm - integer in the range [10… 200]
# Percentage - real number in the interval [0.000… 100.000]

# Exit
# Print a number on the console:
# liters of water that will collect the aquarium.

lenght_sm = int(input())
broad_sm = int(input())
height_sm = int(input())
percent = float(input())

volume_aquarium = lenght_sm * broad_sm * height_sm
volume_in_litters = volume_aquarium * 0.001
occupied_space = percent / 100
needed_litters = volume_in_litters * (1 - occupied_space)
print(needed_litters)
