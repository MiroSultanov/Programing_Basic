# Gabby wants to start a healthy lifestyle and has set a goal of walking 10,000 steps every day. 
# However, some days she is very tired from work and will want to go home before she achieves her goal. 
# Write a program that reads from the console how many steps it takes each time it goes out during the day and when it achieves its goal of writing
# "Goal reached! Good job!" and how many more steps she took "{the difference between the steps} steps over the goal!"
# If she wants to go home before that, she will enter the "Going home" command and enter the steps she took while returning home. 
# Then, if it fails to achieve its goal, the console should read: "{step difference} more steps to reach goal."

target = 10000
total_steps = 0
while total_steps < target:
    command = input()
    if command == 'Going home':
        last_steps = int(input())
        total_steps += last_steps
        break
    current_steps = int(command)
    total_steps += current_steps
diff = abs(total_steps - target)
if total_steps >= target:
    print(f"Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")
