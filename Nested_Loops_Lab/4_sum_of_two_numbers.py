start_int_number = int(input())
final_int_number = int(input())
magic_number = int(input())

combination_counter = 0
breaK_condition = False


for num1 in range(start_int_number, final_int_number + 1):
    for num2 in range(start_int_number, final_int_number + 1):
        combination_counter += 1

        if num1 + num2 == magic_number:
            breaK_condition = True
            print(f"Combination N:{combination_counter} ({num1} + {num2} = {magic_number})")
            break

    if breaK_condition:
        break

if not breaK_condition:
    print(f"{combination_counter} combinations - neither equals {magic_number}")