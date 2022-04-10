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