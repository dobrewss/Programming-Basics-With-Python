nailon = int(input())
paint_per_liter = int(input())
bleach_per_liter = int(input())
hours_work = int(input())

sum_nailon = (nailon + 2) * 1.50
sum_paint = (paint_per_liter + (paint_per_liter * (10/100))) * 14.50
sum_bleach = bleach_per_liter * 5.00
sum_bag = 0.40

whole_price = (sum_nailon + sum_paint + sum_bleach + sum_bag)
price_per_hour = (whole_price*(30/100)) * hours_work

print(whole_price + price_per_hour)


