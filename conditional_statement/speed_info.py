# Write a program that reads the speed (real number) entered by the user and prints speed information.
# ⦁ At slow speeds up to 10 (inclusive) print "slow"
# ⦁ At speeds above 10 and up to 50 (inclusive) print "average"
# ⦁ At speeds above 50 and up to 150 (inclusive) print "fast"
# ⦁ At speeds above 150 and up to 1000 (inclusive) print "ultra fast"
# ⦁ Print "extremely fast" at higher speeds

speed = float(input())
if speed <= 10:
    print('slow')
elif 10 < speed <= 50:
    print('average')
elif 50 < speed <= 150:
    print('fast')
elif 150 < speed <= 1000:
    print('ultra fast')
else:
    print('extremely fast')
