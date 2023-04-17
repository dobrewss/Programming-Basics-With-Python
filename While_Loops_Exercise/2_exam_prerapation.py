max_unpleasing_grades = int(input())

unpleasing_grades = 0
total_grades = 0
grades_sum = 0
last_problem = None

while unpleasing_grades < max_unpleasing_grades:
    task_name = input()

    if task_name == "Enough":
        print(f"Average score: {grades_sum / total_grades:.2f}")
        print(f"Number of problems: {total_grades}")
        print(f"Last problem: {last_problem}")
        break

    grade = int(input())

    if grade <= 4:
        unpleasing_grades += 1

    grades_sum += grade
    total_grades += 1
    last_problem = task_name
else:
    print(f"You need a break, {max_unpleasing_grades} poor grades.")