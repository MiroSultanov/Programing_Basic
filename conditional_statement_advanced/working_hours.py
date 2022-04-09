# Write a program that reads an hour of the day (integer) and a day of the week (text) - entered by the user and checks whether 
# the company's office is open, the office hours are from 10 am to 6 pm, Monday to Saturday including

# Sample input     and   output
#        11Monday        open 
#        19Friday       closed 
#        11Sunday       closed

hour = int(input())
day_of_week = input()
if 10 <= hour <= 18 and day_of_week in 'Monday' 'Tuesday' 'Wednesday' 'Thursday' 'Friday' 'Saturday':
    print('open')
else:
    print('closed')
