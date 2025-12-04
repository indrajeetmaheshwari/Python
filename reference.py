# ----------------------------------------------
# SUPER EASY Student Data Organizer (No functions)
# ----------------------------------------------

students = {}

while True:
    print("\n--- Student Data Organizer ---")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Show All Subjects")
    print("6. Exit")

    choice = input("Enter choice: ")

    # ---------------- ADD STUDENT ----------------
    if choice == "1":
        print("\nAdd Student")

        sid = input("Student ID: ")

        if sid in students:
            print("Student already exists!")
            continue

        name = input("Name: ")
        age = input("Age: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")
        subs = input("Subjects (comma-separated): ")

        # Make subject set
        subject_set = set()
        for s in subs.split(","):
            subject_set.add(s.strip())

        # Tuple for immutability
        id_dob = (sid, dob)

        # Save data
        students[sid] = {
            "id_dob": id_dob,
            "name": name,
            "age": age,
            "subjects": subject_set
        }

        print("Student added!")

    # --------------- DISPLAY STUDENTS ---------------
    elif choice == "2":
        print("\nAll Students:\n")

        if len(students) == 0:
            print("No students yet.")
        else:
            for sid in students:
                s = students[sid]
                print("ID:", sid)
                print("Name:", s["name"])
                print("Age:", s["age"])
                print("Date of Birth:", s["id_dob"][1])
                print("Subjects:", ", ".join(s["subjects"]))
                print("-------------------")

    # --------------- UPDATE STUDENT ----------------
    elif choice == "3":
        print("\nUpdate Student")
        sid = input("Enter Student ID: ")

        if sid not in students:
            print("Student not found.")
            continue

        print("1. Name")
        print("2. Age")
        print("3. Replace Subjects")
        print("4. Add Subject")
        print("5. Remove Subject")

        opt = input("Choose what to update: ")

        if opt == "1":
            students[sid]["name"] = input("New Name: ")
            print("Updated!")

        elif opt == "2":
            students[sid]["age"] = input("New Age: ")
            print("Updated!")

        elif opt == "3":
            subs = input("New subjects (comma-separated): ")
            new_set = set()
            for s in subs.split(","):
                new_set.add(s.strip())
            students[sid]["subjects"] = new_set
            print("Subjects replaced!")

        elif opt == "4":
            new_sub = input("Subject to add: ").strip()
            students[sid]["subjects"].add(new_sub)
            print("Subject added!")

        elif opt == "5":
            rem = input("Subject to remove: ").strip()
            if rem in students[sid]["subjects"]:
                students[sid]["subjects"].remove(rem)
                print("Subject removed!")
            else:
                print("This subject is not in the list.")

        else:
            print("Invalid option.")

    # --------------- DELETE STUDENT ----------------
    elif choice == "4":
        print("\nDelete Student")
        sid = input("Enter Student ID: ")

        if sid in students:
            del students[sid]
            print("Student deleted!")
        else:
            print("Student not found.")

    # --------------- SHOW ALL SUBJECTS -------------
    elif choice == "5":
        print("\nSubjects Offered:")

        all_subs = set()

        for sid in students:
            all_subs.update(students[sid]["subjects"])

        if len(all_subs) == 0:
            print("No subjects available.")
        else:
            for s in all_subs:
                print(s)

    # --------------- EXIT PROGRAM ------------------
    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again.")
