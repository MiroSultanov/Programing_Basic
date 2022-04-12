# Your task is to write a program that calculates the percentage of tickets for each type of ticket sold: student (student), standard (standard) and child (kid),
# for all screenings. You also need to calculate what percentage of the hall is filled for each screening.

# Input
# The input is a series of integers and text:
# ⦁ On the first line until you receive the command "Finish" - movie name - text
# ⦁ In the second row - the free seats in the hall for each screening - integer [1… 100]
# ⦁ For each film, one line is read until the vacancies in the hall are exhausted or until the "End" command is received:
# ⦁ Type of ticket purchased - text ("student", "standard", "kid")

# Output
# The following lines must be printed on the console:
# ⦁ After each film, print what percentage of the cinema is full
# "{movie name} - {percentage of hall full}% full."
# ⦁ When receiving the "Finish" command, print four lines:
# ⦁ "Total tickets: {total number of tickets purchased for all films}"
# } "{Percentage of student tickets}% student tickets."
# ⦁ "{percentage of standard tickets}% standard tickets."
# } "{Percentage of children's tickets}% kids tickets."

student_ticket_counter = 0
standard_ticket_counter = 0
kid_ticket_counter = 0
command = input()
total_ticket_counter = 0
while command != "Finish":
    movie_name = command
    free_places = int(input())
    total_places = free_places
    sold_ticket = 0
    while free_places > 0:
        ticket_type = input()
        if ticket_type == 'End':
            break
        elif ticket_type == "student":
            student_ticket_counter += 1
        elif ticket_type == "standard":
            standard_ticket_counter += 1
        elif ticket_type == "kid":
            kid_ticket_counter += 1
        free_places -= 1
        sold_ticket += 1
        total_ticket_counter += 1
    print(f"{movie_name} - {sold_ticket / total_places * 100:.2f}% full.")
    command = input()
print(f"Total tickets: {total_ticket_counter}")
print(f"{student_ticket_counter / total_ticket_counter * 100:.2f}% student tickets.")
print(f"{standard_ticket_counter / total_ticket_counter * 100:.2f}% standard tickets.")
print(f"{kid_ticket_counter / total_ticket_counter * 100:.2f}% kids tickets.")
