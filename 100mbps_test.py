# Define the functions 

def student():
    student_list = []

    name = input("Please enter you name: ").capitalize()
    surname = input("Please enter you last name: ").capitalize()
    class_name = str(input("Please enter your class: "))

    if name and surname and class_name:
        student_list.append({
            "name" : name,
            "surname" : surname,
            "class" : class_name
            })
    else:
        print("you did not put any info!")
    
    return student_list

def teacher():
    teacher_list = []

    name = input("Please enter you name: ").capitalize()
    surname = input("Please enter you last name: ").capitalize()
    subject = input("Please enter subject of the lesson: ").capitalize()

    classes_taught = []
    while True:
        name_classes = input("Please enter the classes you teach (press enter in empty line to stop): ")

        if name_classes == "":
            break
        else:
            classes_taught.append(name_classes)

    teacher_list.append({
    "name" : name,
    "surname" : surname,
    "subject" : subject,
    "class" : classes_taught
    })

    return teacher_list



def homeroom_teacher():
    homeroom_teacher_list = []

    name = input("Please enter you name: ").capitalize()
    surname = input("Please enter you last name: ").capitalize()
    class_name = str(input("Please enter the class you teach: "))

    if name and surname and class_name:
        homeroom_teacher_list.append({
        "name" : name,
        "surname" : surname,
        "class" : class_name
        })
    else:
        print("you did not put any info!")

    return homeroom_teacher_list


students = []
teachers = []
homeroom_teachers = []

while True:

    print("\nYour options:\n1. create\n2. manage\n3. end!")
    action = input("What would you like to do?: ").lower()

    if action == "3":
        print("\nBye!")
        break

    elif action == "1":
        while True:
             
            print("\nYour options:\n1. student\n2. teacher\n3. homeroom teacher\n4. end!")
            create_action = input("\nWhat would you like to do?: ")

            if create_action == "4":
                print("\nBye bye...")
                break

            elif create_action == "1":
                students.extend(student())
                print(students) # Not needed only for testing

            elif create_action == "2":
                teachers.extend(teacher())
                print(teachers) # Not needed only for testing

            elif create_action == "3":
                homeroom_teachers.extend(homeroom_teacher())
                print(homeroom_teachers) # Not needed only for testing

            else:
                print("Wrong input, please retry")
                continue
    
    elif action == "2":
        while True:
             
            print("\nYour options:\n1. class\n2. student\n3. teacher\n4. homeroom teacher\n5. end!")
            create_action_1 = input("\nPlease type a number: ")



            if create_action_1 == "1":
                class_name = input("Please enter the class: ")
                print(homeroom_teachers)

                students_in_class = [student for student in students if student["class"] == class_name]
                homeroom_teacher_in_class = [home_teacher for home_teacher in homeroom_teachers if home_teacher["class"] == class_name]

                if not students_in_class or not homeroom_teacher_in_class:
                    print("No students or homeroom teacher found for the specified class.")

                else:
                    print("\nStudent(s) in class:")
                    for student_class in students_in_class:
                        print(f"{student_class['name']} {student_class['surname']}")

                    print("\nHomeroom teacher:")
                    print(f"- {homeroom_teacher_in_class[0]['name']} {homeroom_teacher_in_class[0]['surname']}")

            elif create_action_1 == "2":
                while True:
                    student_name = input("Please enter your name: ").capitalize()
                    student_surname = input("Please enter your surname: ").capitalize()

                    students_in_list_name = [student for student in students if student["name"] == student_name and student["surname"] == student_surname]

                    if not students_in_list_name:
                        print("No student found with the specified name and surname.")
                    else:
                        print("\nClass(es) attended by the student:")
                        for student_class_1 in students_in_list_name:
                            print(f"- {student_class_1['class']}")

                        # print("\nTeachers of these classes:")
                        for student_class_t in students_in_list_name:
                            class_name_t = student_class_t['class']
                            teachers_in_class = [teacher_class for teacher_class in teachers if class_name_t in teacher_class["class"]]

                            print(f"\nTeachers for class {class_name_t}:")
                            for teacher_in_class in teachers_in_class:
                                print(f"- {teacher_in_class['name']} {teacher_in_class['surname']}")
                        break

            
            elif create_action_1 == "3":
                teacher_name = input("Please enter your name: ").capitalize()
                teacher_surname = input("Please enter your surname: ").capitalize()

                teacher_classes = [class_t for class_t in teachers if class_t["name"] == teacher_name and class_t["surname"] == teacher_surname]

                if not teacher_classes:
                    print("\nNo avaiable teacher bruah!")

                else:
                    print("\nHere is the class(es):")

                    for t in teacher_classes:
                        class_list = t["class"]
                        if isinstance(class_list, list):
                            for tx in class_list:
                                print(f"- {tx}")

            elif create_action_1 == "4":
                homet_name = input("Please enter your name: ").capitalize()
                homet_surname = input("Please enter your surname: ").capitalize()




            elif create_action_1 == "5":
                print("Bye bye...")
                break


            else:
                print("Wrong input, retry!")


               
         
        


    else:
        print("\nInvalid command!\n")



