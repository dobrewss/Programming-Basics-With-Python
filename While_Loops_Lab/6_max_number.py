number = input()
max_number = int(number)

while number != "Stop":
    num = int(number)

    if num > max_number:
        max_number = num
    number = input()

print(max_number)