import csv

import pytest

'''
access data like data[0] , data[1]
as when used with parameterization it returns data as 
['value1','value2'.....]
'''

def read_csv(file)->list:
    data=[]
    with open(file) as file:
        reader = csv.reader(file,delimiter=';')
        for rows in reader:
            if reader.line_num==1:
                pass
            else:
                data.append(rows)
    return data

# print(read_csv())