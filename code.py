students=[]
while True:
    print("""
        1.Add Students
        2.View Students
        3.Search Students
        4.Exit""")
    choice=int(input("Enter your choice: "))
    if choice==1:
        name=input("Enter student name: ")
        age=int(input("Enter student age: "))
        course=input("Enter student course: ")
        student={"name":name,"age":age,"course":course}
        students.append(student)
        print("Student added successfully!")
    elif choice==2:
        for student in students:
            print(student)
    elif choice==3:
        search=input("Enter the student name to search: ")
        found=False
        for student in students:
            if student["name"]==search:
                print(student)
                found=True
                break    
        if not found:
            print("Student not found!")
    elif choice==4:
        break
    else:
        print("Invalid choice!")