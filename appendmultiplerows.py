#Another way to append rows to csv in folder (when newdata is same for multiple rows): 

import csv 

counter = range(5)

with open('students.csv', 'a', newline='') as graphFile:
    graphFileWriter = csv.writer(graphFile)
    for x in counter:
        graphFileWriter.writerow(['Withdrawn','Withdrawn','Withdrawn','Withdrawn'])
 