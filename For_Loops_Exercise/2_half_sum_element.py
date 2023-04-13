n = int(input())

max_number = float("-inf")
sum_numbers = 0

for _ in range(n):
    number = int(input())
    if number > max_number:
        max_number = number
    sum_numbers += number

if max_number == sum_numbers - max_number:
    print(f"Yes\nSum = {max_number}")
else:
    print(f"No\nDiff = {abs(max_number - (sum_numbers - max_number))}")
