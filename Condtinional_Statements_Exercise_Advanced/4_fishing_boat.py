budget = int(input())
season = input()
fishers = int(input())

boat_rent = 0
total_price = 0


if season == "Spring":
    boat_rent = 3000
    if fishers <= 6:
        total_price = boat_rent * 0.90
    elif 7 <= fishers <= 11:
        total_price = boat_rent * 0.85
    elif fishers > 12:
        total_price = boat_rent * 0.75

if season == "Summer":
    boat_rent = 4200
    if fishers <= 6:
        total_price = boat_rent * 0.90
    elif 7 <= fishers <= 11:
        total_price = boat_rent * 0.85
    elif fishers > 12:
        total_price = boat_rent * 0.75

if season == "Autumn":
    boat_rent = 4200
    if fishers <= 6:
        total_price = boat_rent * 0.90
    elif 7 <= fishers <= 11:
        total_price = boat_rent * 0.85
    elif fishers > 12:
        total_price = boat_rent * 0.75

if season == "Winter":
    boat_rent = 2600
    if fishers <= 6:
        total_price = boat_rent * 0.90
    elif 7 <= fishers <= 11:
        total_price = boat_rent * 0.85
    elif fishers > 12:
        total_price = boat_rent * 0.75

if season == "Spring" and fishers % 2 == 0:
    total_price *= 0.95
if season == "Summer" and fishers % 2 == 0:
    total_price *= 0.95
if season == "Winter" and fishers % 2 == 0:
    total_price *= 0.95

if budget >= total_price:
    print(f'Yes! You have {budget - total_price:.2f} leva left.')

else:
    print(f"Not enough money! You need {total_price - budget:.2f} leva.")