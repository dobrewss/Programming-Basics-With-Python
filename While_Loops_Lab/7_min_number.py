number = input()
min_number = int(number)

while number != "Stop":
    num = int(number)

    if num < min_number:
        min_number = num
    number = input()

print(min_number)