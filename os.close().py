import os


fn = 'file.txt'
file = open(fn, 'r')
ix = file.read()
print(ix)
os.close(ix)


