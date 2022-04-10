# Climbers from all over Bulgaria gather in groups and mark the next peaks to climb. Depending on the size of the group, the climbers will climb different peaks.
# ⦁ Group of up to 5 people - climb Musala
# ⦁ Group of 6 to 12 people - climb Mont Blanc
# ⦁ Group of 13 to 25 people - climb Kilimanjaro
# ⦁ Group of 26 to 40 people - climb K2
# ⦁ A group of 41 or more people - climb Everest
# Write a program that calculates the percentage of climbers climbing each peak.

# Entrance
# A series of numbers are read from the console, each on a separate line:
# ⦁ In the first row - the number of groups of climbers - an integer in the range [1 ... 1000]
# ⦁ For each group on a separate line - the number of people in the group - an integer in the range [1 ... 1000]

# Exit
# Print 5 lines on the console, each containing a percentage between 0.00% and 100.00% to the second digit after the decimal point.
# ⦁ First row - the percentage of climbing Musala
# ⦁ Second row - the percentage of climbers Mont Blanc
# ⦁ Third row - the percentage of climbing Kilimanjaro
# ⦁ Fourth row - the percentage of climbers K2
# ⦁ Fifth row - the percentage of climbing Everest

groups_number = int(input())
group_1 = 0
group_2 = 0
group_3 = 0
group_4 = 0
group_5 = 0
for groups in range(groups_number):
    people_in_group = int(input())
    if people_in_group <= 5:
        group_1 += people_in_group
    elif people_in_group < 13:
        group_2 += people_in_group
    elif people_in_group < 26:
        group_3 += people_in_group
    elif people_in_group < 41:
        group_4 += people_in_group
    else:
        group_5 += people_in_group
all_people = group_1 + group_2 + group_3 + group_4 + group_5
group_1_percent = group_1 / all_people * 100
group_2_percent = group_2 / all_people * 100
group_3_percent = group_3 / all_people * 100
group_4_percent = group_4 / all_people * 100
group_5_percent = group_5 / all_people * 100
print(f"{group_1_percent:.2f}%")
print(f"{group_2_percent:.2f}%")
print(f"{group_3_percent:.2f}%")
print(f"{group_4_percent:.2f}%")
print(f"{group_5_percent:.2f}%")
