# Write a program that calculates a student's average grade throughout his or her studies. On the first line you will receive the student's name, 
# and on each subsequent line his annual grades. The student moves on to the next grade if his / her annual grade is greater than or equal to 4.00. 
# If the student is torn more than once, he is expelled and the program ends by printing the student's name and in which class he is expelled.
#  Upon successful completion of 12th grade to print:
# "{student's name} graduated. Average grade: {average grade from the whole course}"
# In case the student is expelled from school, print:
# "{name of student} has been excluded at {grade} {"
# The value must be formatted to the second decimal place.

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
