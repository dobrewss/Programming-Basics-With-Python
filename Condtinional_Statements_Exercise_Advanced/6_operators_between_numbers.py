number_one = int(input())
number_two = int(input())
operator = input()

total = 0

if number_one == 0 or number_two == 0:
    print(f"Cannot divide {number_one} by zero")
elif operator == "/":
    total = number_one / number_two
    print(f"{number_one} / {number_two} = {total:.2f}")
elif operator == "%":
    total = number_one % number_two
    print(f"{number_one} % {number_two} = {total}")
else:
    if operator == "+":
        total = number_one + number_two
    elif operator == "-":
        total = number_one - number_two
    elif operator == "*":
        total = number_one * number_two
    if total % 2 == 0:
        print(f"{number_one} {operator} {number_two} = {total} - even")
    else:
        print(f"{number_one} {operator} {number_two} = {total} - odd")
