# Ivan decides to improve the World Record for long distance swimming. 
# The console introduces the record in seconds that Ivan has to improve, the distance in meters he has to swim and the time in seconds for which he swims a distance of 1 m. 
# To write a program that calculates whether he has done the task, such as it is considered that: the resistance of the water slows it down every 15 m by 12.5 seconds. 
# When calculating how many times Ivancho will slow down as a result of water resistance, the result should be rounded down to the nearest whole number.
# To calculate the time in seconds for which Ivancho will swim the distance and the difference from the World Record.
 
# Entrance
# 3 lines are read from the console:
# ⦁ The record in seconds - a real number;
# ⦁ The distance in meters - a real number;
# ⦁ The time in seconds for which a distance of 1 m floats - a real number.

# Exit
# Printing the console depends on the result:
# ⦁ If Ivan has improved the World Record (his time is less than the record) we print:
# ⦁ "Yes, he succeeded! The new world record is {Ivan's time} seconds."
# ⦁ If he has NOT improved the record (his time is greater than or equal to the record) we print:
# ⦁ "No, he failed! He was {seconds not slow} seconds slower."
# The result must be formatted to the second decimal place.

old_record = float(input())
distance = float(input())
time_per_meter = float(input())
delay = distance // 15 * 12.5
total_time = distance * time_per_meter +delay
if total_time < old_record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    second_more = abs(total_time - old_record)
    print(f"No, he failed! He was {second_more:.2f} seconds slower.")
