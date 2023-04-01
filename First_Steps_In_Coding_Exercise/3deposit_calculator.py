deposit = float(input())
valid_time = int(input())
gpr = float(input())

final_sum = deposit + valid_time * ((deposit * (gpr / 100) / 12))

print(final_sum)