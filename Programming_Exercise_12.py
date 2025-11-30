# Abrianna Johnson
# 11/23/25

import numpy as np


def load_grades_from_csv(Programming_exersize_CSV):
    # Load the grades from the csv file to this file
    try:
        grades = np.loadtxt(Programming_exersize_CSV, delimiter='\t')
        return grades
    # return the results

    except FileNotFoundError:
        # Print message if the file is not found
        print(f"The file '{Programming_exersize_CSV}' was not found")
        return None

    except Exception as e:
        # print a message if an error occured
        print(f'An error occurred while loading the data: {e}')
        return None


def analyze_grades(grades_array):
    if grades_array is None:
        return
    print(grades_array[:5])
    # Print the first half of the grades

    num_exams = grades_array.shape[1]
    passing_grade = 60
    # Set the passing grade to a 60

    print('Statistics per exam')
    for i in range(num_exams):
        # Print the statistics for the exams
        exam_grades = grades_array[:, i]
        print(f'\nExam {i + 1}:')
        print(f'Mean: {np.mean(exam_grades):.2f}')
        print(f'Median: {np.median(exam_grades):.2f}')
        print(f'Standard Deviation: {np.std(exam_grades):.2f}')
        print(f'Minimum: {np.min(exam_grades):.2f}')
        print(f'Maximum: {np.max(exam_grades):.2f}')

        passed_students = np.sum(exam_grades >= passing_grade)
        # Calculate the students who got a 60 or higher

        failed_students = np.sum(exam_grades < passing_grade)
        # Calculate the students that had a grade less than 60

        print(f'Passed Students: {passed_students}')
        # Print the passing students
        print(f'Failed Students: {failed_students}')
        # Print the failing students

    print("\nOverall Statistics")
    # Print the statistics from all exams
    overall_mean = np.mean(grades_array)
    overall_median = np.median(grades_array)
    overall_std = np.std(grades_array)
    overall_min = np.min(grades_array)
    overall_max = np.max(grades_array)

    print(f"Overall Mean Grade: {overall_mean:.2f}")
    print(f"Overall Median Grade: {overall_median:.2f}")
    print(f"Overall Standard Deviation: {overall_std:.2f}")
    print(f"Overall Minimum Grade: {overall_min:.2f}")
    print(f"Overall Maximum Grade: {overall_max:.2f}")

    overall_passed_count = np.sum(grades_array >= passing_grade)
    # Print the passing students
    overall_total_grades = grades_array.size
    # Print the total grades
    overall_pass_percentage = (overall_passed_count / overall_total_grades) * 100
    print(f"Overall Pass Percentage: {overall_pass_percentage:.2f}%")
    # Print the overall percentage of students that passed


if __name__ == "__main__":
    # Call the function and start the loop
    try:
        with open('Programming_exersize_CSV', 'x') as f:
            f.write("Student,Exam1,Exam2,Exam3\n")

    except FileExistsError:
        pass

grades_data = load_grades_from_csv('Programming_exersize_CSV.py')
# Load grades from the csv file
analyze_grades(grades_data)
# Analyze the grades
