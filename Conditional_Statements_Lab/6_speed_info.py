velocity = float(input())

if velocity <= 10:
    print("slow")
elif 10 < velocity <= 50:
    print("average")
elif 50 < velocity <= 150:
    print("fast")
elif 150 < velocity <= 1000:
    print("ultra fast")
else:
    print("extremely fast")