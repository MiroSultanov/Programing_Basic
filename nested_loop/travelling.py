# destination = input()
# budget = 0
# current_sum = 0
# while destination != "End":
#     money_needed = float(input())
#     while money_needed > budget:
#         current_sum = float(input())
#         budget += current_sum
#     print(f"Going to {destination}!")
#     budget = 0
#     destination = input()
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
