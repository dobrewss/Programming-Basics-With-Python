import math
records_in_seconds = float(input())
meters = float(input())
time_seconds_1meter = float(input())

ivan_time = meters * time_seconds_1meter
suprotivlenie_voda = math.floor(meters / 15) * 12.5

total_time = ivan_time + suprotivlenie_voda
needed_time = total_time - records_in_seconds

if total_time < records_in_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {needed_time:.2f} seconds slower.")