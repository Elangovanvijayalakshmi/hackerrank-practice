#github.com/Elangovanvijayalakshmi

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    rounded_grades = []
    for grade in grades:
        if grade < 38:
            rounded_grades.append(grade)
        else:
            if grade % 5 == 0:
                rounded_grades.append(grade)
            else:
                difference = 0
                new_grade = grade
                while grade % 5 != 0:
                    difference += 1
                    new_grade += 1
                    if new_grade % 5 == 0:
                        break
                if difference < 3:
                    rounded_grades.append(new_grade)
                else:
                    rounded_grades.append(grade)
    return rounded_grades
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
