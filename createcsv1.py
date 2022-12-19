import csv

student_header = ['name', 'society']

student_data = [
    {'name': 'Jack', 'society':'Free Food Society'},
    {'name': 'Sophie', 'society':'Athletes Association'},
    {'name': 'John', 'society':'Gaming Society'},
    {'name': 'Jane', 'society':'Surfing Club'}
]

with open('students1.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=student_header)
    writer.writeheader()
    writer.writerows(student_data) 