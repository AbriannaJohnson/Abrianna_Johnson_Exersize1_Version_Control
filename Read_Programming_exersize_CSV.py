# Abrianna Johnson
# 10/26/25

import csv

def display_grades():
    # Call the grades.csv file to read and display the grades
    with open('grades.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader)

        # Print header
        print(f"{header[0]}, {header[1]} - Grades for: {header[2]}, {header[3]}, {header[4]}")
        # Make a separator line
        print('---------------------------------------------------------------')

        # Print each row
        for row in reader:
            print(f"{row[0]}, {row[1]} - Grades: {row[2]}, {row[3]}, {row[4]}")

display_grades()