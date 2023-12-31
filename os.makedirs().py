import os 

dir_name = 'Java'
dirName = 'Jsscript'
parent_peth = 'C:\\Users\\nibir\\Downloads\\test'

path_join = os.path.join(parent_peth, dir_name)
path_in_js = os.path.join(parent_peth, dirName)

os.makedirs(path_join)
os.makedirs(path_in_js)

print(dir_name)
print(dirName)















