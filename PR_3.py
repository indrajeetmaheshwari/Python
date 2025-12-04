
students = []


while True:
    print("\nWelcome to the Student Data Organizer!\n")

    print("Select any Option")

    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit\n")

    choice = int(input("Enter Your Choice : "))

    if choice == 1:
        print("\nEnter Student Details :~ ")

        student_id = int(input("\nEnter Student ID : "))
        id_exits = 0      

        for i in  range(0, len(students)) :
            stud = students[i]
            if stud['id'] == student_id:
                id_exits = 1
                break

        if id_exits == 1:
              print("This ID already use...")
        else:
            student_name = input("Enter Student Name : ")
            student_age = int(input("Enter Student Age : "))
            student_grade = input("Enter Student Grade : ")
            student_dob = input("Enter Student's Date of Birth : ")
            student_subject = input("Subjects (comma-separated) : ")
            student = {
                        "id": student_id,
                        "name": student_name,
                        "age": student_age,
                        "grade": student_grade,
                        "dob": student_dob,
                        "subjects": student_subject
                    }     
            print("\nStudent Added Successfully!")
            students.append(student)     

    elif choice == 2:
        print("\n--- All Students ---")
   
        # print(students)

        for i in  range(0, len(students)) :
            stud = students[i]
            print(f"Student ID: {stud['id']} | Name: {stud['name']} | Age : {stud['age']} | Grade : {stud['grade']} | Subjects : {stud['subjects']}")
    

    elif choice == 3:
        id = int(input("\nEnter Student ID : "))  
        
        stud_id = 0
        for i in  range(0, len(students)) :
            stud = students[i]

            if stud['id'] ==id :
                stud_id = 1
                student_name = input("Enter Student Name : ")
                student_age = int(input("Enter Student Age : "))
                student_grade = input("Enter Student Grade : ")
                student_dob = input("Enter Student's Date of Birth : ")
                student_subject = input("Subjects (comma-separated) : ")
 
                stud['name'] = student_name
                stud['age'] = student_age
                stud['grade'] = student_grade
                stud['dob'] = student_dob
                stud['subjects'] = student_subject
                break
            else :
                stud_id = 0
        

        if stud_id == 0:
            print("Student Id not found....")
        else : 
            print("Student Updated Successfully...")
    
    elif choice == 4:
        id = int(input("\nEnter Student ID : "))  
        
        stud_id = 0
        for i in  range(0, len(students)) :
            stud = students[i]
            if stud["id"] ==id:
                stud_id = 1
                students.remove(stud)
                break
            else:
                stud_id=0
                
        if stud_id == 0:
            print("Student Id not found....")
        else : 
            print("Student deleted Successfully...")

    elif choice == 5:
        subject=[]
        for i in range(0, len(students)):
            stud = students[i]
            sub = stud["subjects"].split(',')

            for j in range(0, len(sub)):
                subject.append(sub[j])

        print(set(subject))

    elif choice == 6:
        print("  Thank You !! ")
        break