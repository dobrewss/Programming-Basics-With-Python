MAX_POITNS = 1250.5

actor = input()
points = float(input())
judges = int(input())

for _ in range(judges):
    judge_name = input()
    judge_points = float(input())

    points += len(judge_name) * judge_points / 2

    if points > MAX_POITNS:
        print(f"Congratulations, {actor} got a nominee for leading role with {points:.1f}!")
        break
else:
    print(f"Sorry, {actor} you need {MAX_POITNS - points:.1f} more!")