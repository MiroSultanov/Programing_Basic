# Write a program that reads the day of the week (text), in English - entered by the user. 
# If the day is working prints on the console - "Working day", if it is a holiday - "Weekend". 
# If text other than the day of the week is entered, print "Error".

# Sample input and output
# Input Output
# Monday Working day

# Input Output
# Sunday Weekend

# Input Output
# April Error

day_of_week = input()
if day_of_week == 'Monday':
    print("Working day")
elif day_of_week == 'Tuesday':
    print("Working day")
elif day_of_week == 'Wednesday':
    print("Working day")
elif day_of_week == 'Thursday':
    print("Working day")
elif day_of_week == 'Friday':
    print("Working day")
elif day_of_week == 'Saturday':
    print("Weekend")
elif day_of_week == 'Sunday':
    print("Weekend")
else:
    print("Error")
