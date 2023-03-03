database = {}

'''
Students are allowed to consult their grades in classes their names are present.
In this sense, to research information, the program must ask for their name to seek from the dicionaries
'''

def line_separator(biggest_string_len, number_of_columns):
    separator = "*"
    for i in range(number_of_columns):
        separator += ("-" * (biggest_string_len + 2)) + "*"
    return separator

def line_print(biggest_string_len, number_of_columns, line_header, grades):
    line = f'| {line_header.center(biggest_string_len)} |'
    for i in range(number_of_columns):
        line += f' {grades[i].center(biggest_string_len)} |'
    return line


def student_search(student_name):
    # Subject column format
    biggest_string = len("Subject Name")
    biggest_columns = 0
    student_subjects = []

    # Student information search and format adaptations
    for subject in database:
        if student_name in database[subject][2].keys():
            student_subjects.append(subject)
            if len(subject) > biggest_string:
                biggest_string = len(subject)
            if len(database[subject][2][student_name]) > biggest_columns:
                biggest_columns = len(database[subject][2][student_name])
    header_grades = []
    for i in range(1, biggest_columns + 1):
        header_grades.append(f'Grade {i}')

    if len(student_subjects) != 0:
        # Student greet and program information
        print(f'Welcome, {student_name}!\nBelow are your grades so far...')

        # Display
        separator = line_separator(biggest_string, biggest_columns)
        print(separator)
        print(line_print(biggest_string, biggest_columns, "Subject Name", header_grades))
        for student_subject in sorted(student_subjects):
            grades = database[student_subject][2][student_name]
            line_print(biggest_string, biggest_columns, student_subject, grades)


    else: # Student not registered in any classes
        print(f'{student_name}, you are not registered in any classes...')


'''
Teachers will be allowed to modify or add student grades as long as their passwords are correct
To register class and password a teacher must know the school code which will be "school code"
'''

def name_check(teacher_name):
    unique = True
    for subject in database:
        if database[subject][0] == teacher_name:
            unique = False
            break
    return unique


def teacher_gathering(): # returns tuple with subject name, teacher name, password, and number of grades
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
    print("Perfect! Let's keep going!")
    while subject_cond:
        subject_name = input("Type in the class name: ")
        if subject_name not in database.keys():
            subject_cond = False
        else:
            print("Another teacher is alreadying using the class name typed. Try another...")

    # Number of grades number check
    grades_cond = True
    print("Alright! To finish the setup!")
    while grades_cond:
        number_of_grades = input("Finally, how many grades would you like the class to have? ")
        if not number_of_grades.isalpha():
            if number_of_grades.isdigit():
                grades_cond = False
                number_of_grades = int(number_of_grades)
            else:
                print("The typed number isn't an integer. Try again...")
        else:
            print("The typed number isn't a number. Try again...")


    return subject_name, [teacher_name, teacher_password, number_of_grades, {}]


def teacher_info(teacher_name):
    for subject in database:
        if database[subject][0] == teacher_name:
            return subject, database[subject]


def teacher_login():
    print("Please type the login information below...")
    login_cond = True
    while login_cond:
        teacher_name = input("Please type your name: ")
        if not name_check(teacher_name): # checks if name is in database
            teacher_subject, teacher_subject_info = teacher_info(teacher_name)
            teacher_password = input("Please register a password: ")
            if teacher_password == teacher_subject_info[1]:
                login_cond = False
            else: # incorrect password
                print("Incorrect password. Try again...")
        else:
            print("It seems you haven't registred a class...")
            ans = input("Would you like to register a class?(yes/no) ")
            if ans.lower() == "yes":
                teacher_signup()
            else:
                 print("Perhaps you mispelled your name. Try again...")
    return teacher_name, teacher_subject, teacher_subject_info


def teacher_signup():
    database_key, database_value = teacher_gathering()
    database[database_key] = database_value
    print(f'All done!\nYour class has been registred, {database_value[0]}.')
    return teacher_login()


def teacher_commands(teacher_subject):
    cont_cond = True
    while cont_cond:
        print("Command Options:\n"
              "1 - Add student\n"
              "2 - Update student grade\n"
              "3 - Search student\n"
              "4 - List students grades\n"
              "5 - End session")
        option = input("Which command would you like to perform: ")

        if option == "1":
            student_name = input("What is the student name you would like to add? ")
            if student_name not in database[teacher_subject][3]:
                database[teacher_subject][3][student_name] = database[teacher_subject][2] * ["-"]
            else:
                print("There is already a student in your class with the name typed. Try again...")

        elif option == "2":
            student_name = input("What is the student's name you would like to alter grades? ")
            if student_name in database[teacher_subject][3]:
                print(f'Here are {student_name} grades so far:')
                grades = database[teacher_subject][3][student_name]
                for i in range(1, len(grades) + 1):
                    print(f'Grade {i} - {grades[i] - 1}')
                update_which = input("Which one would you like to alter? ")
                if update_which in range(1, len(grades)):
                    update_value = input("What is the updated value (between 0 and 10)? ")
                    if update_value.isalpha() == False:
                        if 10 >= float(update_value) >= 0:
                            database[teacher_subject][3][student_name][int(update_which) - 1] = update_value
                        else:
                            print("The typed number isn't in the interval defined. Try again...")
                    else:
                        print("String typed isn't a number. Try again...")
                else:
                    print("Invalid option. Try again...")
            else:
                print("There isn't a student in your class with the name typed. Try again...")

        elif option == "3":
            student_name = input("Which student would you like to search grades? ")
            if student_name in database[teacher_subject][3]:
                if len("Student Name") > len(student_name):
                    biggest_string = len("Student Name")
                else:
                    biggest_string = len(student_name)
                sep = "*" + ("-" * (biggest_string + 2)) + "*" \
                      + ("-" * (biggest_string + 2)) + "*" \
                      + ("-" * (biggest_string + 2)) + "*" \
                      + ("-" * (biggest_string + 2)) + "*"
                print(sep)
                line_print(biggest_string, "Subject Name", " Grade 1 ", " Grade 2 ", " Grade 3 ")  # Header line
                grades = database[teacher_subject][3][student_name]
                line_print(biggest_string, student_name, grades[0], grades[1], grades[2])
            else:
                print("There isn't a student in your class with the name typed. Try again...")

        elif option == "4":
            students = database[teacher_subject][3]
            biggest_string = len("Student Name")
            for student in students:
                if len(student) > biggest_string:
                    biggest_string = len(student)
            sep = "*" + ("-" * (biggest_string + 2)) + "*" \
                  + ("-" * (biggest_string + 2)) + "*" \
                  + ("-" * (biggest_string + 2)) + "*" \
                  + ("-" * (biggest_string + 2)) + "*"
            print(sep)
            line_print(biggest_string, "Subject Name", " Grade 1 ", " Grade 2 ", " Grade 3 ") # Header line
            for student in sorted(students):
                grades = database[teacher_subject][3][student]
                line_print(biggest_string, student, grades[0], grades[1], grades[2])

        elif option == "5":
            cont_cond = False
        else:
            print("Please type a valid option. Try again...")


def teacher_access():
    access_cond = True
    while access_cond:
        if input("Type the teacher access password provided by the program: ") == "teacher":
            access_cond = False
        else:
            print("The typed access password is incorrect.")
            student = input("Would you like to return to the main page?(yes/no) ")
            if student.lower() == "yes":
                access_cond = False
                main()


def main():
    main_cond = True
    print("Welcome to the school grading system!")
    while main_cond:
        persona = input("Are you a student or teacher? ")
        if persona == "teacher":
            teacher_access()
            account_cond = True
            while account_cond:
                signed = input("Are you already signed up?(yes/no) ")
                if signed.lower() == "yes":
                    teacher_name, teacher_subject, teacher_subject_info = teacher_login()
                    account_cond = False
                elif signed.lower() == "no":
                    teacher_name, teacher_subject, teacher_subject_info = teacher_signup()
                    account_cond = False
                else:
                    print("Invalid option. Try again...")
            teacher_commands(teacher_subject)
            print(f'Thank you, {teacher_name}! Come back anytime...')
        elif persona == "student":
            student_search(input("Type your name to do the search: "))
        else:
            print("Please type student or teacher. Try again...")
        keep_going = input("Would you like to keep going?(yes/no) ")
        if keep_going.lower() == "no":
            main_cond = False
    print("Logging off...")

main()