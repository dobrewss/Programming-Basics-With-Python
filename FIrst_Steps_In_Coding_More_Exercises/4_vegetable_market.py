price_vegetables_kg = float(input())

price_fruits_kg = float(input())

vegetables_kg = int(input())

fruits_kg = int(input())

vegetables = price_vegetables_kg*vegetables_kg

fruits = price_fruits_kg*fruits_kg

sum = vegetables + fruits

sum_to_euro = sum/1.94
print(f"{sum_to_euro:.2f}")