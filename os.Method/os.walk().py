#Code Here Write
import os

dri_path = r'C:\Users\nibir\Downloads\test'
deta = os.walk(dri_path)

for root, dir_name, file in deta:
    print(root)
    print(dir_name)
    print(file)
    print("-----------------------------")
    





