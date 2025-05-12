import csv
import os
import pytest

'''
access data like data[0] , data[1]
as when used with parameterization it returns data as 
['value1','value2'.....]
'''

def read_csv(relative_path) -> list:
    data = []
    # Build absolute path relative to project root
    base_dir = os.path.dirname(os.path.abspath(__file__))  # utils/
    file_path = os.path.abspath(os.path.join(base_dir, '..', relative_path))

    with open(file_path, newline='') as file:
        reader = csv.reader(file, delimiter=';')
        for rows in reader:
            if reader.line_num == 1:
                continue
            data.append(rows)
    return data

# print(read_csv())