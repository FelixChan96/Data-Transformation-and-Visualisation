#Edit the CSV file within the folder: 

from csv import writer
List = [['Samantha',26,'Computer Science', 'Data Science'],
        ['Bruce', 25, 'Economics','Finance']]
with open('students.csv','a') as f_object:
    writer_object=writer(f_object)
    writer_object.writerow(List)
    f_object.close()    
    