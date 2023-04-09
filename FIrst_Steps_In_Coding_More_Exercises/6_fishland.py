skumriq_kg = float(input())
caca_kg = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = int(input())

midi = 7.50

palamud = skumriq_kg + (skumriq_kg * 0.6)
sum_palamud = palamud * palamud_kg
safrid = caca_kg + (caca_kg * 0.8)
sum_safrid = safrid * safrid_kg

print(f"{sum_palamud + sum_safrid + (midi_kg * midi):.2f}")
