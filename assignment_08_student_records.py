# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def display_menu():
    """Display the student record system menu."""
    print("===============================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("===============================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


def add_student(students):
    """Add a new student record to the list."""
    name = input("Student name: ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return

    try:
        student_id = int(input("Student ID: "))
    except ValueError:
        print("Error: Student ID must be a number.")
        return

    if any(student["id"] == student_id for student in students):
        print("Error: A student with that ID already exists.")
        return

    try:
        score_count = int(input("How many scores? "))
    except ValueError:
        print("Error: Please enter a valid integer for the number of scores.")
        return

    if score_count < 0:
        print("Error: Number of scores cannot be negative.")
        return

    scores = []
    for i in range(1, score_count + 1):
        while True:
            try:
                score = float(input(f"Enter score {i}: "))
                scores.append(score)
                break
            except ValueError:
                print("Error: Please enter a valid numeric score.")

    student = {
        "name": name,
        "id": student_id,
        "scores": scores,
    }
    students.append(student)
    print(f'Student "{name}" added successfully.')


def display_all_students(students):
    """Display all students in a formatted table."""
    if not students:
        print("No students have been added yet.")
        return

    print("--------------------------------------------------")
    print(f"{'Name':<15} {'ID':<10} {'Scores':<20} {'Average'}")
    print("--------------------------------------------------")
    for student in students:
        scores_text = ", ".join(str(int(score) if score.is_integer() else score) for score in student["scores"])
        average = calculate_average(student)
        print(f"{student['name']:<15} {student['id']:<10} {scores_text:<20} {average:.2f}")
    print("--------------------------------------------------")


def calculate_average(student):
    """Return the average score for a student record."""
    if not student["scores"]:
        return 0.0
    return sum(student["scores"]) / len(student["scores"])


def calculate_average_for_student(students):
    """Prompt for a student ID and show the student's average score."""
    try:
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print("Error: Student ID must be a number.")
        return

    for student in students:
        if student["id"] == student_id:
            average = calculate_average(student)
            print(f"{student['name']}'s average score: {average:.2f}")
            return

    print("Error: Student ID not found.")


def main():
    """Run the student record management system."""
    students = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_all_students(students)
        elif choice == "3":
            calculate_average_for_student(students)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Please enter a choice from 1 to 4.")
        print()


if __name__ == "__main__":
    main()

