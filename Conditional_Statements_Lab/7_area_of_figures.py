import math
figure = input()
a = float(input())

if figure == "square":

    print(f"{a ** 2:.3f}")

elif figure == "rectangle":

    print(f"{a * float(input()):.3f}")

elif figure == "circle":

    print(f"{math.pi * (a*a):.3f}")

elif figure == "triangle":

    print(f"{a * float(input()) / 2:.3f}")