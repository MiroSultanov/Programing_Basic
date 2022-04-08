# Write a program that reads a password (text) entered by the user and checks if the entered password matches the phrase "s3cr3t! P @ ssw0rd". 
# In case of coincidence, display "Welcome".
# In case of discrepancy, display "Wrong password!".

user_password = 's3cr3t!P@ssw0rd'
input_password = input()
if user_password == input_password:
    print('Welcome')
else:
    print('Wrong password!')
