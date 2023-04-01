pack_pen = int(input())
pack_marker = int(input())
liter_detergent = int(input())
discout = int(input()) / 100

final_price = (pack_pen * 5.80) + (pack_marker * 7.20) + (liter_detergent * 1.20)
final_price_discount = final_price - (final_price * discout)

print(final_price_discount)
