needed_money = float(input())
money_on_hand = float(input())
type_of_action = ' '
days_counter = 0
spend_counter = 0
while money_on_hand < needed_money and spend_counter < 5:
    command = input()
    money = float(input())
    days_counter += 1
    if command == 'save':
        money_on_hand += money
        spend_counter = 0
    elif command == 'spend':
        money_on_hand -= money
        spend_counter += 1
        if money_on_hand < 0:
            money_on_hand = 0
if spend_counter == 5:
    print(f"You can't save the money.")
    print(days_counter)
if money_on_hand >= needed_money:
    print(f"You saved the money for {days_counter} days.")