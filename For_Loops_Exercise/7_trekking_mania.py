groups = int(input())

musala = 0
monlban = 0
kilimanjaro = 0
k2 = 0
everest = 0
for _ in range(groups):
    group = int(input())

    if group < 6:
        musala += group
    elif group < 13:
        monlban += group
    elif group < 26:
        kilimanjaro += group
    elif group < 41:
        k2 += group
    else:
        everest += group

total_people = musala + monlban + kilimanjaro + k2 + everest

print(f"{musala / total_people * 100:.2f}%")
print(f"{monlban / total_people * 100:.2f}%")
print(f"{kilimanjaro / total_people * 100:.2f}%")
print(f"{k2 / total_people * 100:.2f}%")
print(f"{everest / total_people * 100:.2f}%")