budget = float(input())
season = input()

price = 0
destination = ""
type_holiday = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        price = budget * 0.30
        type_holiday = "Camp"
    elif season == "winter":
        price = budget * 0.70
        type_holiday = "Hotel"

if 101 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        price = budget * 0.40
        type_holiday = "Camp"
    elif season == "winter":
        price = budget * 0.80
        type_holiday = "Hotel"
if budget > 1000:
    destination = "Europe"
    type_holiday = "Hotel"
    price = budget * 0.90

print(f"Somewhere in {destination}")
print(f"{type_holiday} - {price:.2f}")

