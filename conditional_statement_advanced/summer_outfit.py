# Summer is a season with very changeable weather and Victor needs your help. 
# Write a program that, depending on the time of day and the degrees, will recommend Victor what clothes to wear. 
# Your friend has different plans for each stage of the day, which require a different look - you can see them from the table.
# Exactly two lines are read from the console:
# ⦁ Degrees - integer;
# ⦁ Time of day - text with three options "Morning", "Afternoon" or "Evening".

# Time of day / degrees	       Morning	               Afternoon	             Evening
# 10 <= градуси <= 18	     Outfit = Sweatshirt          Outfit = Shirt            Outfit = Shirt
#                          Shoes = Sneakers	         Shoes = Moccasins         Shoes = Moccasins
    
# 18 < градуси <= 24	     Outfit = Shirt              Outfit = T-Shirt          Outfit = Shirt
#                          Shoes = Moccasins	         Shoes = Sandals           Shoes = Moccasins

# градуси >= 25	        Outfit = T-Shirt            Outfit = Swim Suit         Outfit = Shirt 
#                         Shoes = Sandals	            Shoes = Barefoot           Shoes = Moccasins
	

degree = int(input())
time_of_the_day = input()
shoes = " "
outfit = " "
if time_of_the_day == 'Morning':
    if 10 <= degree <= 18:
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif 18 < degree <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif degree >= 25:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
elif time_of_the_day == 'Afternoon':
    if 10 <= degree <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < degree <= 24:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif degree >= 25:
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
elif time_of_the_day == 'Evening':
    if 10 <= degree <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < degree <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif degree >= 25:
        outfit = 'Shirt'
        shoes = 'Moccasins'
print(f"It's {degree} degrees, get your {outfit} and {shoes}.")
