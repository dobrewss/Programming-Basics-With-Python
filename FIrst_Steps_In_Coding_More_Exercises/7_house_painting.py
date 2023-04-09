x = float(input())
y = float(input())
h = float(input())

green_per_liter = 3.4
red_per_liter = 4.3

front_wall = (x * x) - (1.2 * 2)
front_and_back_wall = (x * x) + front_wall

side_walls = ((x * y) - (1.5 * 1.5)) * 2

roof_side = (x * y) * 2
roof_front = (x * h / 2) * 2

whole_sides = (front_and_back_wall + side_walls) / green_per_liter
whole_roof = (roof_front + roof_side) / red_per_liter

print(f"{whole_sides:.2f}")
print(f"{whole_roof:.2f}")




