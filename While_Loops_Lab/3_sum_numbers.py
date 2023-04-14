CONSTANT_NUMBER = int(input())

sum_number = 0

while True:
    current_number = int(input())
    sum_number += current_number

    if sum_number >= CONSTANT_NUMBER:
        print(sum_number)
        break