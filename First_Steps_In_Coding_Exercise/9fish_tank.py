lenght = int(input())
width = int(input())
height = int(input())
percent = float(input()) / 100

# 1 liter = 1 cub decimeter = total / 1000

whole_litres = (lenght * width * height) / 1000
full_tank = whole_litres * ( 1 - percent)

print(full_tank)