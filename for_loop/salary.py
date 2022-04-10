# A company boss notices that more and more employees are spending time on sites that distract them.
# To prevent this, he introduces surprise checks on the open tabs of his employees' browsers.
# According to the open site, the following fines are imposed in the tab:
# "" Facebook "-> BGN 150.
# ⦁ "Instagram" -> BGN 100.
# ⦁ "Reddit" -> BGN 50.
# Two lines are read from the console:
# ⦁ Number of open tabs in the browser n - integer in the range [1 ... 10]
# ⦁ Salary - a number in the interval [500 ... 1500]
# Then n - the name of the website - text is read a number of times
# Input
# 10
# 750
# Facebook
# Dev.bg
# Instagram
# Facebook
# Reddit
# Facebook
# Facebook

# Output
# ⦁ If during the inspection the salary becomes less than or equal to BGN 0, the console shows
# "You have lost your salary." and the program ends.
# ⦁ Otherwise, after checking the console, the rest of the salary is displayed (to be written as an integer).

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
