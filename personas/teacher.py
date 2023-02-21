'''
Teachers will be allowed to modify or add student grades as long as their passwords are correct
To register class and password a teacher must know the school code which will be "school code"
'''

database = {}

def name_check(teacher_name):
    unique = True
    for subject in database:
        if database[subject][0] == teacher_name:
            unique = False
            break
    return unique


def teacher_information(): # returns tuple with subject name, teacher name, and password
    # Unique name check
    name_cond = True
    print("Alright, let's register your class!")
    while name_cond:
        teacher_name = input("Please type your name: ")
        if name_check(teacher_name):
            name_cond = False
        else:
            print("Please type in your full name since another teacher has already registered the typed name...")

    # Confirm password check
    password_cond = True
    print(f'Great, {teacher_name}!')
    while password_cond:
        teacher_password = input("Please register a password: ")
        confirm_password = input("Confirm the password typed above: ")
        if teacher_password == confirm_password:
            password_cond = False
        else:
            print("The passwords aren't the same, please try again...")

    # Unique subject name check
    subject_cond = True
    print("Perfect! Let's finish the class setup!")
    while subject_cond:
        subject_name = input("Finally type in the class name: ")
        if subject_name not in database.keys():
            subject_cond = False
        else:
            print("Another teacher is alreadying using the class name typed. Try another...")

    return subject_name, [teacher_name, teacher_password, {}]


def teacher_info(teacher_name):
    for subject in database:
        if database[subject][0] == teacher_name:
            return subject, database[subject]


def teacher_login():
    print("Please type the login information below...")
    login_cond = True
    while login_cond:
        teacher_name = input("Please type your name: ")
        teacher_password = input("Please register a password: ")
        if not name_check(teacher_name): # checks if name is in database
            teacher_subject, teacher_subject_info = teacher_info(teacher_name)
            if teacher_password == teacher_subject_info[1]:
                login_cond = False
            else: # incorrect password
                print("Incorrect password. Try again...")
        else:
            print("It seems you haven't registred a class...")
            ans = input("Would you like to register a class? ")
            if ans.lower() == "yes":
                teacher_signup()
            else:
                 print("Perhaps you mispelled your name. Try again...")
    return teacher_name, teacher_subject, teacher_subject_info


def teacher_signup():
    database_key, database_value = teacher_information()
    database[database_key] = database_value
    print(f'All done!\nYour class has been registred, {database_value[0]}.')
    teacher_login()


def teacher_commands():
    cont_cond = True
    while cont_cond:
        print("Command Options:\n"
              "1 - Update student grade\n"
              "2 - Search student\n"
              "3 - List students grades\n"
              "4 - End session")
        option = int(input("Which command would you like to perform: "))
        if option == 1:
            print()
        elif option == 2:
            print()
        elif option == 3:
            print()
        elif option == 4:
            cont_cond = False
        else:
            print("Please type a valid option. Try again...")



'''
Students are allowed to consult their grades in classes their names are present.
In this sense, to research information, the program must ask for their name to seek from the dicionaries
'''

def line_print(subject_format, subject_name, grade1, grade2, grade3):
    print(f'| {subject_name.center(subject_format)} | {grade1} | {grade2} | {grade3} |')

def student_search(class_database, student_name):
    # Subject column format
    biggest_string = len("Subject Name")
    student_subjects = []

    # Student information search
    for subject in class_database:
        if student_name in class_database[subject][2].keys():
            student_subjects.append(subject)
            if len(subject) > biggest_string:
                biggest_string = len(subject)
    if len(student_subjects) != 0:
        # Student greet and program information
        print(f'Welcome, {student_name}!\nBelow are your grades so far...')

        # Display
        sep = "*" + ("-" * (biggest_string + 2)) + "*---------*---------*---------*"
        print(sep)
        line_print(biggest_string, "Subject Name", " Grade 1 ", " Grade 2 ", " Grade 3 ") # Header line
        print(sep)
        for student_subject in student_subjects:
            student_grades = class_database[student_subject][2][student_name]
            line_print(biggest_string, student_subject, student_grades[0], student_grades[1], student_grades[2])
            print(sep)

    else: # Student not registered in any classes
        print(f'{student_name}, you are not registered in any classes...')


def main():
    cond = True
    print("Welcome to the school grading system!")
    while cond:
        persona = input("Are you a student or teacher?")
        if persona == "teacher":
            cond = False
        elif persona == "student":
            cond = False
        else:
            print("Please type student or teacher. Try again...")

