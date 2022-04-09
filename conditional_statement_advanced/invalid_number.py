# A number is valid if it is in the range [100… 200] or is 0. Write a program that reads an integer entered by the user and print "invalid" 
# if the number entered is not valid.
# Sample input and output
# entrance exit entrance exit entrance exit entrance exit
# Input    Output
# 75       invalid 
# 150      (no exit) 
# 220      invalid 
# 199     (no exit)
# -1       invalid 
# 100      (no exit) 
# 200      (no exit)
# 0        (no exit)


number = int(input())
if 100 <= number <= 200 or number == 0:
    pass
else:
    print("invalid")
