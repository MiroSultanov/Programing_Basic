# Write a program that calculates how many hours it will take an architect to design several construction projects. The preparation of a project takes three hours.

# Entrance
# 2 lines are read from the console:
# ⦁ The name of the architect - text
# ⦁ Number of projects to be prepared - integer in the range [0… 100]
# Exit

# The following is printed on the console:
# "The architect {name of architect} will need {required hours} hours to complete {number of projects} project / s."

name = input()
number_of_projects = int(input())

time_to_complete_project = number_of_projects * 3
print(f"The architect {name} will need {time_to_complete_project} hours to complete "
      f"{number_of_projects} project/s.")
