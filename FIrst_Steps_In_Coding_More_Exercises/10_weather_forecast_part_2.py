weather = float(input())

if 26.00 <= weather <= 35.00:
    print("Hot")
elif 20.1 <= weather <= 25.9:
    print("Warm")
elif 15.00 <= weather <= 20.00:
    print("Mild")
elif 12.00 <= weather <= 14.9:
    print("Cool")
elif 5.00 <= weather <= 11.9:
    print("Cold")
else:
    print("unknown")