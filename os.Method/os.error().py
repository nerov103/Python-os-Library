#import Library
import os 

try:
    file_name = 'file.txt'
    with open(file_name, 'r') as f:
        f.read()
        f.close()
except FileNotFoundError:
    print('Problem reading: ' + file_name)



