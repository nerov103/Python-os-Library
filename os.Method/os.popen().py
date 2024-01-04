import os

fn = 'file.txt'
file_open = open(fn, 'w')
file_open.write('My Name is Nerov Ahmad \n ima From bangladesh \n i red in class ten')
file_open.close()

#file Try red and open
with open(fn, 'r') as ex:
    read_mod = ex.read()
    print(read_mod)

#Agin Oprn  this file
agin_open = os.popen(fn, 'w')
agin_open.write('Hello world!')





