#Generate CSV file in folder using Python:

import csv

student_header = ['name', 'age', 'major', 'minor']

student_data = [
    {'name': 'Jack', 'age': 23, 'major': 'Physics', 'minor': 'Chemistry'},
    {'name': 'Sophie', 'age': 22, 'major': 'Physics', 'minor': 'Computer Science'},
    {'name': 'John', 'age': 24, 'major': 'Mathematics', 'minor': 'Physics'},
    {'name': 'Jane', 'age': 30, 'major': 'Chemistry', 'minor': 'Physics'}
]

with open('students.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=student_header)
    writer.writeheader()
    writer.writerows(student_data) 