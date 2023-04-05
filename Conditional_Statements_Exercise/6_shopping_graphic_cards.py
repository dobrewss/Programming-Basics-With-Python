budget = float(input())
graphic_cards_count = int(input())
cpu_count = int(input())
ram_count = int(input())

gpu_price = 250

graphic_cards_price = graphic_cards_count * gpu_price
cpu_price = cpu_count * graphic_cards_price * 0.35
ram_price = ram_count * graphic_cards_price * 0.10

total_price = graphic_cards_price + cpu_price + ram_price

if graphic_cards_count > cpu_count:
    total_price *= 0.85

if total_price <= budget:
    print(f"You have {budget - total_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_price - budget:.2f} leva more!")