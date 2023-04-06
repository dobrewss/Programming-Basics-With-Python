type = input()
rows = int(input())
columns = int(input())


total_price = 0


Premiere_ticket = 12.00
Normal_ticket = 7.50
Discount_ticket = 5.00

cinema_capacity = rows * columns

if type == "Premiere":
    total_price = cinema_capacity * Premiere_ticket
    print(f"{total_price:.2f} leva")
if type == "Normal":
    total_price = cinema_capacity * Normal_ticket
    print(f"{total_price:.2f} leva")
if type == "Discount":
    total_price = cinema_capacity * Discount_ticket
    print(f"{total_price:.2f} leva")