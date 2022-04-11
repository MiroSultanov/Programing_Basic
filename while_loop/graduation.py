name = input()
grade = 0
year = 0
sum_of_grades = 0
failed_class = 0
while grade < 12:
    grade = float(input())
    if grade >= 4.00:
        year += 1
        sum_of_grades += grade
    if grade < 4.00:
        failed_class += 1
        if failed_class > 1:
            year += 1
            print(f"{name} has been excluded at {year} grade")
            break
    elif year == 12:
        average_grades = sum_of_grades / 12
        print(f"{name} graduated. Average grade: {average_grades:.2f}")
        break