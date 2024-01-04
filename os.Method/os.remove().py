import os

file_name = 'Java'
perant_path = 'C:\\Users\\nibir\\Downloads\\test'
join_path = os.path.join(perant_path, file_name)

os.remove(join_path)
print(f'{file_name} remove success!!')




#write by Nerov Ahmad
