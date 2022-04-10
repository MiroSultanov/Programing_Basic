from math import floor

number_of_cargo = int(input())
cargo_t = 0
total_cargo = 0
average_price_per_tone = 0
percent_per_tone = 0
bus_cargo = 0
truck_cargo = 0
train_cargo = 0
for cargo in range(number_of_cargo):
    total_cargo += cargo_t
    price_per_ton = int(input())
    if cargo_t <= 3:
        price_per_ton += 200
    elif 4 < cargo_t < 11:
        price_per_ton += 175
    else:
        price_per_ton += 120
average_price_per_tone = cargo_t / number_of_cargo
bus_cargo = cargo_t / total_cargo * 100
truck_cargo = cargo_t / total_cargo * 100
train_cargo = cargo_t / total_cargo * 100
print(f"{floor(average_price_per_tone):.2f}")
print(f"{bus_cargo:.2f}%")
print(f"{truck_cargo:.2f}%")
print(f"{train_cargo:.2f}%")


