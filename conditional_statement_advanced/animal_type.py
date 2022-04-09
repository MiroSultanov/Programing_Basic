# Write a program that prints the class of the animal according to its name entered by the user.
# ⦁ dog -> mammal
# ⦁ crocodile, tortoise, snake -> reptile
# ⦁ others -> unknown

# Sample input and output
# Input   Output
# dog    mammal
# snake  reptile
# cat   unknown

type_of_animal = input()
if type_of_animal == 'dog':
    print("mammal")
elif type_of_animal == 'crocodile' or type_of_animal == 'tortoise' or type_of_animal == 'snake':
    print("reptile")
else:
    print("unknown")
