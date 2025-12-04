students = []   # List to store student details

while True:
    print("\nWelcome to the Student Data Organizer!\n")
    print("Select an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # ---------------------- ADD STUDENT -------------------------
    if choice == "1":
        print("\nEnter student details:\n")

        student_id = input("Student ID: ")
        name = input("Name: ")
        age = input("Age: ")
        grade = input("Grade: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")
        subjects = input("Subjects (comma-separated): ")

        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "grade": grade,
            "dob": dob,
            "subjects": [s.strip() for s in subjects.split(",")]
        }

        students.append(student)
        print("\nStudent added successfully!\n")

    # ---------------------- DISPLAY ALL STUDENTS -------------------------
    elif choice == "2":
        print("\n--- All Students ---")
        if not students:
            print("No students found.\n")
        else:
            for s in students:
                print(f"\nStudent ID: {s['id']}")
                print(f"Name: {s['name']}")
                print(f"Age: {s['age']}")
                print(f"Grade: {s['grade']}")
                print(f"Date of Birth: {s['dob']}")
                print(f"Subjects: {', '.join(s['subjects'])}")
            print()

    # ---------------------- UPDATE STUDENT -------------------------
    elif choice == "3":
        roll = input("\nEnter Student ID to update: ")

        found = False
        for s in students:
            if s["id"] == roll:
                print("\nEnter new details (leave blank to keep previous):")

                new_name = input("New Name: ")
                new_age = input("New Age: ")
                new_grade = input("New Grade: ")
                new_dob = input("New Date of Birth (YYYY-MM-DD): ")
                new_subjects = input("New Subjects (comma-separated): ")

                if new_name != "":
                    s["name"] = new_name
                if new_age != "":
                    s["age"] = new_age
                if new_grade != "":
                    s["grade"] = new_grade
                if new_dob != "":
                    s["dob"] = new_dob
                if new_subjects != "":
                    s["subjects"] = [x.strip() for x in new_subjects.split(",")]

                print("\nStudent information updated!\n")
                found = True
                break

        if not found:
            print("Student not found.\n")

    # ---------------------- DELETE STUDENT -------------------------
    elif choice == "4":
        roll = input("\nEnter Student ID to delete: ")

        deleted = False
        for s in students:
            if s["id"] == roll:
                students.remove(s)
                print("Student deleted successfully!\n")
                deleted = True
                break

        if not deleted:
            print("Student not found.\n")

    # ---------------------- DISPLAY SUBJECTS -------------------------
    elif choice == "5":
        print("\nSubjects Offered in System:")
        subjects_list = set()  # collect unique subjects
        for s in students:
            for sub in s["subjects"]:
                subjects_list.add(sub)

        if subjects_list:
            for sub in subjects_list:
                print(f"- {sub}")
        else:
            print("No subjects stored yet.")
        print()

    # ---------------------- EXIT -------------------------
    elif choice == "6":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice! Try again.\n")
