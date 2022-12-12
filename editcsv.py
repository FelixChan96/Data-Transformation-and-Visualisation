#Edit the CSV file within the folder: 

from csv import writer
List = ['G7',1240,17]
with open('students.csv','a') as f_object:
    writer_object=writer(f_object)
    writer_object.writerow(List)
    f_object.close()    
    