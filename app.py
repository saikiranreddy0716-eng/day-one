
def get_valid_name():
    while True:
        name = input("Enter student name: ").strip()

        if name:
            return name

        print("Error: Name cannot be empty.")


def get_valid_age():
    while True:
        age_input = input("Enter student age: ").strip()

        try:
            age = int(age_input)

            if age <= 0:
                print("Error: Age must be greater than 0.")
                continue

            return age

        except ValueError:
            print("Error: Please enter a whole number for age.")


def get_valid_marks(subject_name):
    while True:
        marks_input = input(
            f"Enter {subject_name} marks (0-100): "
        ).strip()

        try:
            marks = float(marks_input)

            if marks < 0 or marks > 100:
                print("Error: Marks must be between 0 and 100.")
                continue

            return marks

        except ValueError:
            print("Error: Please enter a valid number for marks.")


def main():
    print("\n=== Student Marks Calculator ===")

    student_name = get_valid_name()
    student_age = get_valid_age()

    python_marks = get_valid_marks("Python")
    maths_marks = get_valid_marks("Maths")

    total_marks = python_marks + maths_marks
    average_marks = total_marks / 2

    result = "PASS" if average_marks >= 40 else "FAIL"

    print("\n========== STUDENT REPORT ==========")
    print(f"Student Name : {student_name}")
    print(f"Student Age  : {student_age}")
    print(f"Python Marks : {python_marks:.2f}")
    print(f"Maths Marks  : {maths_marks:.2f}")
    print(f"Total Marks  : {total_marks:.2f} / 200")
    print(f"Average      : {average_marks:.2f}")
    print(f"Result       : {result}")
    print("===================================")


if __name__ == "__main__":
    main()
