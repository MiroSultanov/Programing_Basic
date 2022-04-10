You are invited by the academy to write software to calculate the points for an actor / actress. The academy will give you initial points for the actor. 
# Then each evaluator will give his evaluation. The points that the actor receives are formed by: the length of the evaluator's name multiplied
# by the points he gives divided by two. If the result at some point exceeds 1250.5 the program must be interrupted and it must be printed 
# that the actor has received a nomination.

# Entrance
# ⦁ Actor's name - text
# ⦁ Academy points - real number in the interval [2.0 ... 450.5]
# ⦁ Number of estimators n - integer in the interval [1… 20]
# The next n number of rows:
# ⦁ Name of the evaluator - text
# ⦁ Assessor points - real number in the range [1.0 ... 50.0]

# Exit
# Print one line on the console:
# ⦁ If the points are above 1250.5:
# "Congratulations, {actor's name} got a nominee for leading role with {points}!"
# ⦁ If the points are not enough:
# "Sorry, {actor's name} you need {need points} more!"
# The result should be formatted to the first digit after the decimal point!

actor_name = input()
total_points = float(input())
number_of_jury = int(input())
for current_grade in range(number_of_jury):
    current_name = input()
    current_point = float(input())
    current_final_points = len(current_name) * current_point / 2
    total_points += current_final_points
    if total_points >= 1250.5:
        break
if total_points > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
else:
    difference = 1250.5 - total_points
    print(f"Sorry, {actor_name} you need {difference:.1f} more!")
