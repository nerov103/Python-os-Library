import os 

dir_name = 'Java'
parent_path = 'C:\\Users\\nibir\\Downloads\\test'
join_dir = os.path.join(parent_path, dir_name)

print(os.listdir(parent_path))
os.rmdir(join_dir)
print(parent_path)



