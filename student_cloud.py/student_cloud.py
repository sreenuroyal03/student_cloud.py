
# Cloud-Based Student Record System

students = []

while True:
    print("\n===== STUDENT CLOUD SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        course = input("Enter course name: ")

        students.append({
            "name": name,
            "roll": roll,
            "course": course
        })

        print("Student record saved successfully!")

    elif choice == "2":
        if not students:
            print("No student records found.")
        else:
            print("\n--- Student Records ---")
            for student in students:
                print("Name:", student["name"])
                print("Roll Number:", student["roll"])
                print("Course:", student["course"])
                print("----------------------")

    elif choice == "3":
        roll = input("Enter roll number to search: ")
        found = False

        for student in students:
            if student["roll"] == roll:
                print("Student Found!")
                print("Name:", student["name"])
                print("Course:", student["course"])
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "4":
        print("Student Cloud System Closed.")
        break

    else:
        print("Invalid choice. Try again.")
