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

# Testing funcion above
student_search({}, input("Hello!\nType in your name to check out your grades: "))