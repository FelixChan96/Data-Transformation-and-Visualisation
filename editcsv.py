#edit csv file: 

from csv import writer
List = ['Joseph',22,'Computer Science','Data Science']
with open('machinesdata.csv','a') as f_object:
    writer_object=writer(f_object)
    writer_object.writerow(List)
    f_object.close()    
    