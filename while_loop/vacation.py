# Jesse has decided to raise money for a trip and asks you to help her find out if she will be able to raise the necessary amount. 
# She saves or spends some of her money every day. If she wants to spend more than her cash, she will spend as much as she has and she will have 0 leva left.

# Input
# From the console read:
# ⦁ Money needed for the trip - real number;
# ⦁ Cash - real number.
# Then two lines are read repeatedly:
# ⦁ Type of action - text with two options: "spend" or "save";
# ⦁ The amount you will save / spend - a real number.

# Output
# The program must be completed in the following cases:
# ⦁ If Jesse only spends 5 consecutive days, the console should show:
# ⦁ "You can't save the money."
# ⦁ "{Total days passed}"
# ⦁ If Jesse collects the money for the holiday, the console says:
# ⦁ "You saved the money for {total days passed} days."

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
