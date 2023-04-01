year_tax = int(input())

basketball_shoes = year_tax - (year_tax * 0.40)
basketball_suit = basketball_shoes - (basketball_shoes * 0.20)
basketball_ball = basketball_suit / 4
basketball_accs = basketball_ball / 5

total_price = year_tax + basketball_shoes + basketball_suit + basketball_ball + basketball_accs

print(total_price)
