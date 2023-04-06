temp = int(input())
day_type = input()

outfit = None
shoes = None

if 10 <= temp <= 18:
    if day_type == "Morning":
        outfit = "Sweatshirt"
        shoes = "Sneakers"
        print(f"It's {temp} degrees, get your {outfit} and {shoes}.")
    elif day_type == "Afternoon" or day_type == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
        print(f"It's {temp} degrees, get your {outfit} and {shoes}.")

if 18 < temp <= 24:
    if day_type == "Morning" or day_type == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
        print(f"It's {temp} degrees, get your {outfit} and {shoes}.")
    elif day_type == "Afternoon":
        outfit = "T-Shirt"
        shoes = "Sandals"
        print(f"It's {temp} degrees, get your {outfit} and {shoes}.")

if temp >= 25:
    if day_type == "Morning":
        outfit = "T-Shirt"
        shoes = "Sandals"
        print(f"It's {temp} degrees, get your {outfit} and {shoes}.")
    elif day_type == "Afternoon":
        outfit = "Swim Suit"
        shoes = "Barefoot"
        print(f"It's {temp} degrees, get your {outfit} and {shoes}.")
    elif day_type == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
        print(f"It's {temp} degrees, get your {outfit} and {shoes}.")