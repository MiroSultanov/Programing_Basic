# Write a program that initially reads a username and password. Then read the login password.
# ⦁ when entering the wrong password: prompt the user to enter a new password.
# ⦁ when entering the correct password: print "Welcome {username}!".

username = input()
password = input()
current_password = " "
while current_password != password:
    current_password = input()
print(f"Welcome {username}!")
