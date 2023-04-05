cena_ekskurziq = float(input())
broi_puzel = int(input())
broi_kukli = int(input())
broi_mecheta = int(input())
broi_minioni = int(input())
broi_kamioni = int(input())

total_price = \
    (broi_puzel * 2.60) + \
    (broi_kukli * 3) + \
    (broi_mecheta * 4.10) + \
    (broi_minioni * 8.20) + \
    (broi_kamioni * 2)
obshto_igrachki = \
    broi_puzel + \
    broi_kukli + \
    broi_mecheta + \
    broi_minioni + \
    broi_kamioni

if obshto_igrachki >= 50:
    total_price = total_price * 0.75

total_price = total_price * 0.90

if total_price >= cena_ekskurziq:
    print(f"Yes! {total_price - cena_ekskurziq:.2f} lv left.")
else:
    print(f"Not enough money! {cena_ekskurziq - total_price:.2f} lv needed.")