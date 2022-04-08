# Write a program in which the user enters the type and dimensions of a geometric figure and calculates its face. The figures are of four types: 
# square, square, rectangle, circle and triangle. The first line of the input reads the type of figure (text with the following options: square, rectangle, 
# circle or triangle).
# ⦁ If the figure is a square: the next line reads a fractional number - the length of its side
# ⦁ If the figure is a rectangle: on the next two lines read two fractional numbers - the lengths of its sides
# ⦁ If the figure is a circle: on the next line reads a fractional number - the radius of the circle
# ⦁ If the figure is a triangle: the next two lines read two fractional numbers - the length of its side and the length of the height to it
# Round the result to 3 digits after the decimal point.


from math import pi

figure = input()
if figure == 'square':
    num1 = float(input())
    result = num1 * num1
    print(f'{result:.3f}')

elif figure == 'rectangle':
    num1 = float(input())
    num2 = float(input())
    result = num1 * num2
    print(f'{result:.3f}')

elif figure == 'circle':
    num1 = float(input())
    result = pi * (num1 ** 2)
    print(f'{result:.3f}')

elif figure == 'triangle':
    num1 = float(input())
    num2 = float(input())
    result = (num1 * num2) / 2
    print(f'{result:.3f}')
