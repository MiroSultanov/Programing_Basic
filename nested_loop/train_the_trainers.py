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
