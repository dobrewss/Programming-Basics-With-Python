student_name = input()
grades_total = 0
year_counter = 0
failed_counter = 0

while True:
    current_year_grade = float(input())

    if current_year_grade < 4:
        failed_counter += 1
        if failed_counter == 2:
            print(f"{student_name} has been excluded at {year_counter + 1} grade")
            break

    else:
        year_counter += 1
        grades_total += current_year_grade
        if year_counter == 12:
            average_grade = grades_total / 12
            print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
            break