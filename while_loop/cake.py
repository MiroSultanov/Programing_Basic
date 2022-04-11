# You are invited to the 30th birthday, when the birthday boy eats a huge cake. However, he does not know how many pieces his guests can take from her. 
# Your task is to write a program that calculates the number of pieces that guests have taken before it ends. You will get the dimensions of the 
# cake (width and length - integers and then on each line, until you receive the command "STOP" or until the cake is finished, the number of 
# pieces that guests take from it. Each piece of cake is 1x1 cm .
# Print one of the following lines on the console:
# "{Number of pieces} pieces are left." - if you reach STOP and the pieces of cake are not finished;
#  "No more cake left! You need {number of missing pieces} pieces more."

width = int(input())
length = int(input())
cake_pieces = width * length
cake_is_over = False
command = input()
while command != "STOP":
    current_number_of_pieces = int(command)
    cake_pieces -= current_number_of_pieces
    if cake_pieces < 0:
        cake_is_over = True
        break
    command = input()
if cake_is_over:
    print(f"No more cake left! You need {abs(cake_pieces)} pieces more.")
else:
    print(f"{cake_pieces} pieces are left.")
