from math import floor

tournaments = int(input())
starting_points = int(input())

win_tournaments = 0
gained_points = 0

for _ in range(tournaments):
    result = input()

    if result == "W":
        win_tournaments += 1
        gained_points += 2000
    elif result == "F":
        gained_points += 1200
    elif result == "SF":
        gained_points += 720

print(f"Final points: {gained_points + starting_points}")
print(f"Average points: {floor(gained_points / tournaments)}")
print(f"{win_tournaments / tournaments * 100:.2f}%")
