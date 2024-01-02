import os


dir_path = 'C:\\Users\\nibir\\Downloads\\test\\Java'
os.chdir(dir_path)

os.rename('file.txt', 'update.csv')
print(os.listdir())


