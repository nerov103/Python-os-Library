import os

path = 'C:\\Users\\nibir\\Downloads\\test'
os.chdir(path)
if os.path.exists('Jsscript.com'):
    print(True)
else:
    print('Sorry!')


