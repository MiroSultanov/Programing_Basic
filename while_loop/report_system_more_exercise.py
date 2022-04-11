expected_amount = int(input())
amount_is_enough = False
amount_cs = 0
amount_cc = 0
cc_count = 0
cs_count = 0
price = input()
count = 1
while price != "End":
    price = int(price)
    if count % 2 != 0 and price <= 100:
        amount_cs += price
        cs_count += 1
        average_cs = amount_cs / cs_count
        print(f"Product sold!")
    elif count % 2 == 0 and price >= 10:
        amount_cc += price
        cc_count += 1
        average_cc = amount_cc / cc_count
        print(f"Product sold!")
    else:
        print(f"Error in transaction!")
    if amount_cs + amount_cc >= expected_amount:
        amount_is_enough = True
        break
    price = input()
    count += 1
if amount_is_enough:
    print(f"Average CS: {average_cs:.2f}")
    print(f"Average CC: {average_cc:.2f}")
else:
    print(f"Failed to collect required money for charity.")