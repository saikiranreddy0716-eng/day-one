def get_valid_name():
    while True:
        name = input("Enter student name: ").strip()

        if name:
            return name

        print("Error: Name cannot be empty.")


def get_valid_marks():
    while True:
        marks_input = input("Enter marks (0-100): ").strip()

        try:
            marks = float(marks_input)

            if 0 <= marks <= 100:
                return marks

            print("Error: Marks must be between 0 and 100.")

        except ValueError:
            print("Error: Please enter a valid number.")


def get_result(marks):
    if marks >= 40:
        return "PASS"
    return "FAIL"


def main():
    students = []

    print("=== Student Data Processor ===")

    while True:
        name = get_valid_name()
        marks = get_valid_marks()

        student = {
            "name": name,
            "marks": marks,
            "result": get_result(marks)
        }

        students.append(student)

        choice = input("Add another student? (yes/no): ").strip().lower()

        if choice != "yes":
            break

    passed_students = [
        student for student in students
        if student["result"] == "PASS"
    ]

    print("\n========== STUDENT REPORT ==========")

    for student in students:
        print(
            f"Name: {student['name']} | "
            f"Marks: {student['marks']:.2f} | "
            f"Result: {student['result']}"
        )

    average_marks = (
        sum(student["marks"] for student in students)
        / len(students)
    )

    print("------------------------------------")
    print(f"Total students : {len(students)}")
    print(f"Passed         : {len(passed_students)}")
    print(f"Failed         : {len(students) - len(passed_students)}")
    print(f"Class average  : {average_marks:.2f}")
    print("====================================")


if __name__ == "__main__":
    main()