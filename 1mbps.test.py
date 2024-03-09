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
                students = student()

            elif create_action == "2":
                teachers = teacher()

            elif create_action == "3":
                homeroom_teachers = homeroom_teacher()

            else:
                print("Wrong input, please retry")
                continue
    
    elif action == "2":
        while True:
             
            print("\nYour options:\n1. class\n2. student\n3. teacher\n4. homeroom teacher\n5. end!")
            create_action_1 = input("\nPlease type just a number: ")

            if create_action_1 == "1":
                class_name = input("Please enter the class: ")
                while True:
                    if class_name == students["class"] and class_name == homeroom_teachers["class"]:
                        break
                    else:
                        print("Invalid class, Please try again!")

                for key, value in students.items(): #and homeroom_teachers.items():
                    if key == "class":
                        print(f"{key}: {value}")
         
        


    else:
        print("\nInvalid command!\n")



