number_of_opening_tabs = int(input())
salary = int(input())
name_of_the_website = " "
total_money = 0
for page in range(number_of_opening_tabs):
    page = input()
    if page == 'Facebook':
        salary -= 150
    elif page == 'Instagram':
        salary -= 100
    elif page == 'Reddit':
        salary -= 50
        total_money = number_of_opening_tabs - salary
    if salary <= 0:
        print(f"You have lost your salary.")
        break
else:
    difference = salary - total_money
    print(difference)