month = input()
night_count = int(input())

studio_price = 0
apartment_price = 0
total_ap = 0
total_studio = 0

if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
    if 7 < night_count < 14:
        studio_price *= 0.95
    elif night_count > 14:
        studio_price *= 0.70

if month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70
    if night_count > 14:
        studio_price *= 0.80

if month == 'July' or month == "August":
    studio_price = 76
    apartment_price = 77

if night_count > 14:
    apartment_price *= 0.90

total_ap = apartment_price * night_count
total_studio = studio_price * night_count

print(f"Apartment: {total_ap:.2f} lv.")
print(f"Studio: {total_studio:.2f} lv.")