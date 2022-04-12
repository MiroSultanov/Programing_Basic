# The "Train the trainers" course is coming to an end and the final evaluation is approaching. Your task is to help the jury that will 
# evaluate the presentations by writing a program in which to calculate the average grade from the performance of each presentation by a student, 
# and finally - the average success of all of them.
# From the console in the first row is read the number of people on the jury n - an integer.
# Then the name of the presentation is read on a separate line - text.
# For each presentation on a new line read n - the number of marks - a real number.
# After calculating the average score for a specific presentation, the following is printed on the console:
#  "{presentation name} - {average grade}."
# After receiving the "Finish" command, the console reads "Student's final assessment is {average of all presentations}." and the program ends.
# All grades must be formatted to the second decimal place.

number_of_jury = int(input())
name_of_presentation = input()
total_degrees_of_all_presentation = 0
counter_of_degree = 0
average_degree = 0
while name_of_presentation != "Finish":
    total_degrees = 0
    for people in range(1, number_of_jury + 1):
        current_degree = float(input())
        counter_of_degree += 1
        total_degrees += current_degree
    average_degree = total_degrees / number_of_jury
    total_degrees_of_all_presentation += total_degrees
    print(f"{name_of_presentation} - {average_degree:.2f}.")
    name_of_presentation = input()
print(f"Student's final assessment is {total_degrees_of_all_presentation / counter_of_degree:.2f}.")
