# Define the functions 

def student():
    student_list = []

    name = input("Please enter you name: ").capitalize()
    surname = input("Please enter you last name: ").capitalize()
    class_name = input("Please enter your class: ").upper()

    if name and surname and class_name:
        student_list.append({
            "name" : name,
            "surname" : surname,
            "class" : class_name
            })
    else:
        print("\nYou did not provide all the info, please retry!")
    
    return student_list

def teacher():
    teacher_list = []
    while True:
        try:
            name = input("Please enter you name: ").capitalize()
            surname = input("Please enter you last name: ").capitalize()
            subject = input("Please enter subject of the lesson: ").capitalize()

            if not name or not surname or not subject:
                raise ValueError()
            
        except ValueError:
            print("\nAll the info are required, please retry!")
            break
        

        classes_taught = []
        while True:
            print("\nPlease note: to save your details at least 1 class need to be added!\n")
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
        
        break


    return teacher_list


# def teacher():
#     teacher_list = []

#     name = input("Please enter you name: ").capitalize()
#     surname = input("Please enter you last name: ").capitalize()
#     subject = input("Please enter subject of the lesson: ").capitalize()

#     classes_taught = []
#     while True:
#         name_classes = input("Please enter the classes you teach (press enter in empty line to stop): ").upper()

#         if name_classes == "":
#             break

#         elif name and surname and subject:
#             teacher_list.append({
#             "name" : name,
#             "surname" : surname,
#              "subject" : subject,
#             })
#             print(f"name no class? {teacher_list}")
        
#         else:
#             classes_taught.append(name_classes)
#             print(f"with class?? {teacher_list}")

#     teacher_list.append({
#     "class" : classes_taught
#     })
#     print(f"Is this all???? {teacher_list}")


#     return teacher_list


def homeroom_teacher():
    homeroom_teacher_list = []

    name = input("Please enter you name: ").capitalize()
    surname = input("Please enter you last name: ").capitalize()
    class_name = input("Please enter the class you teach: ").upper()

    if name and surname and class_name:
        homeroom_teacher_list.append({
        "name" : name,
        "surname" : surname,
        "class" : class_name
        })
    else:
        print("\nyou did not put any info!")

    return homeroom_teacher_list


students = []
teachers = []
homeroom_teachers = []

while True:

    print("\nYour options:\n1. create\n2. manage\n3. end")
    action = input("\nPlease type a number: ").lower()

    if action == "3":
        print("\nSee you soon :)\n")
        break

    elif action == "1":
        while True:
             
            print("\nYour options:\n1. student\n2. teacher\n3. homeroom teacher\n4. end")
            create_action = input("\nPlease type a number: ")

            if create_action == "4":
                print("\nBye bye...")
                break

            elif create_action == "1":
                students.extend(student())

            elif create_action == "2":
                teachers.extend(teacher())

            elif create_action == "3":
                homeroom_teachers.extend(homeroom_teacher())

            else:
                print("\nWrong input, please retry")
                continue
    
    elif action == "2":
        while True:
             
            print("\nYour options:\n1. class\n2. student\n3. teacher\n4. homeroom teacher\n5. end")
            create_action_1 = input("\nPlease type a number: ")

            if create_action_1 == "1":
                class_name = input("Please enter the class: ").upper()

                students_in_class = [student for student in students if student["class"] == class_name]
                homeroom_teacher_in_class = [home_teacher for home_teacher in homeroom_teachers if home_teacher["class"] == class_name]

                if not students_in_class or not homeroom_teacher_in_class:
                    print("\nNo students or homeroom teacher found for the specified class.")

                else:
                    print("\nStudent(s) in class:")
                    for student_class in students_in_class:
                        print(f"{student_class['name']} {student_class['surname']}")

                    print("\nHomeroom teacher:")
                    print(f"- {homeroom_teacher_in_class[0]['name']} {homeroom_teacher_in_class[0]['surname']}")

            elif create_action_1 == "2":
                    student_name = input("Please enter your name: ").capitalize()
                    student_surname = input("Please enter your surname: ").capitalize()

                    students_in_list_name = [student for student in students if student["name"] == student_name and student["surname"] == student_surname]

                    if not students_in_list_name:
                        print("\nNo student found with the specified name and surname.")
                    else:
                        print("\nClass attended by the student:")
                        for student_class_1 in students_in_list_name:
                            print(f"- {student_class_1['class']}")

                        for student_class_t in students_in_list_name:
                            class_name_t = student_class_t['class']
                            teachers_in_class = [teacher_class for teacher_class in teachers if class_name_t in teacher_class["class"]]

                            print(f"\nTeachers for class {class_name_t}:")
                            for teacher_in_class in teachers_in_class:
                                print(f"- {teacher_in_class['name']} {teacher_in_class['surname']}")
         
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

                home_room_teach = [home_teach for home_teach in homeroom_teachers if home_teach["name"] == homet_name and home_teach["surname"] == homet_surname]

                if not home_room_teach:
                        print("\nNot available!")
                else:
                    homeroom_students = []
                    for student_home in students:

                        if student_home["class"] == home_room_teach[0]["class"]:
                            homeroom_students.append(f"- {student_home['name']} {student_home['surname']}")

                    if homeroom_students:
                        print(f"\nThe homeroom teacher {homet_name} {homet_surname} leads the below student(s):")
                        print("\n".join(homeroom_students))
                        
                    else:
                        print("\nNo students found for this homeroom teacher.")

            elif create_action_1 == "5":
                print("\nBye bye...")
                break

            else:
                print("\nWrong input, retry!")

    else:
        print("\nInvalid command!\n")



