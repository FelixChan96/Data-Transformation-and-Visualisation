from csv import writer
List = ['Samantha',19,'Computer Science','Data Science']
with open('students.csv','a') as f_object:
    writer_object=writer(f_object)
    writer_object.writerow(List)
    f_object.close()    
    