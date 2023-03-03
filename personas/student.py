'''
Students are allowed to consult their grades in classes their names are present.
In this sense, to research information, the program must ask for their name to seek from the dicionaries
'''

database = {}

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
    student_subjects = []

    # Student information search
    for subject in database:
        if student_name in database[subject][2].keys():
            student_subjects.append(subject)
            if len(subject) > biggest_string:
                biggest_string = len(subject)
    if len(student_subjects) != 0:
        # Student greet and program information
        print(f'Welcome, {student_name}!\nBelow are your grades so far...')

        # Display
        sep = "*" + ("-" * (biggest_string + 2)) + "*" \
              + ("-" * (biggest_string + 2)) + "*" \
              + ("-" * (biggest_string + 2)) + "*" \
              + ("-" * (biggest_string + 2)) + "*"
        print(sep)
        line_print(biggest_string, "Subject Name", " Grade 1 ", " Grade 2 ", " Grade 3 ") # Header line
        for student_subject in student_subjects:
            grades = database[student_subject][2][student_name]
            line_print(biggest_string, student_subject, grades[0], grades[1], grades[2])


    else: # Student not registered in any classes
        print(f'{student_name}, you are not registered in any classes...')
