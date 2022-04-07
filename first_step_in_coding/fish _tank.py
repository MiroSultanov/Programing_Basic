lenght_sm = int(input())
broad_sm = int(input())
height_sm = int(input())
percent = float(input())

volume_aquarium = lenght_sm * broad_sm * height_sm
volume_in_litters = volume_aquarium * 0.001
occupied_space = percent / 100
needed_litters = volume_in_litters * (1 - occupied_space)
print(needed_litters)