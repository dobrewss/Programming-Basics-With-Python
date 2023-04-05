budget = float(input())
statisti = int(input())
cena_statist = float(input())

decor = budget * 0.10

if statisti > 150:
    cena_statist = cena_statist * 0.90

total_expenses = decor + statisti * cena_statist

if total_expenses <= budget:
    print(f"Action! \nWingard starts filming with {abs(budget - total_expenses):.2f} leva left.")
else:
    print(f"Not enough money! \nWingard needs {abs(budget - total_expenses):.2f} leva more.")