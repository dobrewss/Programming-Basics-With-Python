grade_count = int(input())

grade = 0
average_grade = 0

while True:
    exam = input()
    grade_at_the_time = int(input())
    grade += 1
    if grade_at_the_time <= 4:
        if grade == grade_count:
            break

    if exam == "Enough":
        grade_at_the_time += 1
        average_grade = grade_at_the_time / grade
        print(f"Average score: {average_grade}")
        break
