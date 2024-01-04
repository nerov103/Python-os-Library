import  os

'''create_dir_path = os.getcwd()
join_path = os.path.join(create_dir_path, 'info.txt')
path, exction_nm = os.path.splitext(join_path)


# print(path, end=" ")
# print(exction_nm)
all_file_name = os.listdir()
for i in all_file_name:
    x, y = os.path.splitext(create_dir_path)
    print(x)
    if y !='.py':
        print(y)
    else:
        print(x,y)
'''

crate_path = os.getcwd()
sorch = os.path.join(crate_path, 'Updateinfo.txt')
destenection = os.path.join(f"{crate_path}\\Hero\\PersonalFile.txt")

os.rename(sorch, destenection)



