# Define the functions 

def student():
    student_list = []

    name = input("Please enter you name: ").capitalize()
    surname = input("Please enter you last name: ").capitalize()
    class_name = input("Please enter your class: ")

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
        name_classes = input("Please enter the classes you teach: ")

        if name_classes == "":
            break
        else:
            classes_taught.append(name_classes)

    teacher_list.append({
    "name" : name,
    "surname" : surname,
    "subject" : subject,
    "name class or classes" : classes_taught
    })

    return teacher_list


# print(teacher())


def homeroom_teacher():
    homeroom_teacher_list = []

    name = input("Please enter you name: ").capitalize()
    surname = input("Please enter you last name: ").capitalize()
    class_name = input("Please enter the class you teach: ").capitalize()

    if name and surname and class_name:
        homeroom_teacher_list.append({
            "name" : name,
            "surname" : surname,
            "class" : class_name
        })
    else:
        print("you did not put any info!")

    return homeroom_teacher_list







# print(student())

# students = student()
      
# for k, v in students.items():
#     print(f"- {k.capitalize()}: {v}")


# Inital programbasdb
# student = []
# teacher = []
# homeroom_teacher = []




while True:

    print("\nYour options: create, manage, end!")
    action = input("What would you like to do?: ").lower()

    if action == "end":
        print("\nBye!")
        break

    elif action == "create":
        while True:
             
            print("\nYour options: student, teacher, homeroom teacher or end!")  # .strip()
            create_action = input("\nWhat would you like to do?: ").lower()

            if create_action == "end":
                print("\nBye bye...")
                break

            elif create_action == "student":
                students = student()
                for stud in students:
                    print()  
                    for k, v in stud.items(): # This can be removed it is only for me to see the result
                        print(f"- {k.capitalize()}: {v}") # This can be removed it is only for me to see the result

            elif create_action == "teacher":
                teachers = teacher()

                # for k1, v1 in teachers.items(): # This can be removed it is only for me to see the result
                #     print(f"- {k1.capitalize()}: {v1}") # This can be removed it is only for me to see the result

            elif create_action == "homeroom teacher":
                homeroom_teachers = homeroom_teacher()

                # for k2, v2 in homeroom_teachers.items(): # This can be removed it is only for me to see the result
                #     print(f"- {k2.capitalize()}: {v2}") # This can be removed it is only for me to see the result

            else:
                print("Wrong input, please retry")
                continue
    
    elif action == "manage":

        while True:
            
            print("\nYour options: student, teacher, homeroom teacher, class or end!")  # .strip()
            create_action_1 = input("\nWhat would you like to do?: ").lower()

            
            if create_action_1 == "end":
                print("Bye Bye Bye...")
                break

            elif create_action_1 == "class":

                student_class_list = student()
                homeroom_teacher_list = homeroom_teacher()

                while True:
                    class_list = input("\nWhich class would you like to check?: ")
                    if class_list == student_class_list["class"] or class_list == homeroom_teacher_list["class"]:
                        break
                    else:
                        print("\nClass not found!")

                for k3, v3 in student_class_list.items() or homeroom_teacher_list.items():
                    if k3 != "class":
                        print(f"- {k3.capitalize()}: {v3}")


                    









    else:
        print("\nInvalid command!\n")