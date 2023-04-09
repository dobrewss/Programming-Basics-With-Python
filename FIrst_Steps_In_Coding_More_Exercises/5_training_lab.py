w = float(input()) * 100
h = float(input()) * 100



rows = w//120

h_to_cm = h - 100

buros_in_rows = h_to_cm//70

all_buros = rows*buros_in_rows - 3

print(f"{all_buros:.0f}")