while True:
    destination = input()

    if destination == "End":
        break

    excursion_price = float(input())
    current_money = 0

    while excursion_price > current_money:
        current_money += float(input())

    print(f"Going to {destination}!")
    