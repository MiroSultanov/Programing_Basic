# Annie loves to travel and wants to visit several different destinations this year. When she chooses a destination, she will decide how much money 
# she will need to get there, and she will start saving. When she has saved enough, she will be able to travel.
# The destination and the minimum budget (decimal number) that will be needed for the trip will be read from the console each time.
# Then a few sums (decimal numbers) will be read, which Annie saves by working and when she manages to collect enough for the trip,
# she will leave, and the console should say: "Going to {destination}!"
# When she has visited all the destinations she wants, instead of a destination she will enter "End" and the program will end. 


destination = input()
budget = 0
current_sum = 0
for current_sum in range(budget):
    needed_money = float(input())
    if destination == "End":
        break
    if needed_money >= budget:
        print(f"Going to {destination}!")
        budget = 0
        destination = input()
