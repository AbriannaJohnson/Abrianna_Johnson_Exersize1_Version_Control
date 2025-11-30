# Abrianna Johnson
# 10/26/25

import csv

def write_grades():
    # Prompt the user to enter number of students
    num_students = int(input('Enter the number of students: '))

    with open('grades.csv', 'w', newline='') as file:
        # Write the csv file
        writer = csv.writer(file)
        # Create the rows for name and exam number
        writer.writerow(['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])

        for _ in range(num_students):
            # Prompt the user for names and grades for each exam
            first_name = input("Enter the student's first name: ")
            last_name = input("Enter the student's last name: ")
            exam1 = int(input('Enter Exam 1 grade: '))
            exam2 = int(input('Enter Exam 2 grade: '))
            exam3 = int(input('Enter Exam 3 grade: '))
            # Format the row with the name and grade
            writer.writerow([first_name, last_name, exam1, exam2, exam3])
    print('Grades successfully written')

# Call the main function
write_grades()