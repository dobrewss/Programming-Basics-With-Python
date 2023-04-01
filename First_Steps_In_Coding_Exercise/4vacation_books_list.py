pages = int(input())
pages_per_hour = int(input())
days = int(input())

hours = (pages / pages_per_hour) / days
print(int(hours))