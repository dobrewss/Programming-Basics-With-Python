chicken_menu = float(input()) * 10.35
fish_menu = float(input()) * 12.40
vegan_menu = float(input()) * 8.15
delivery = 2.50

sum_menu = chicken_menu + fish_menu + vegan_menu

dessert_price = sum_menu * (20/100)

final_price = sum_menu + dessert_price + delivery

print(f"{final_price:.2f}")