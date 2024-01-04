import os

now_crate_path = os.getcwd()
print(now_crate_path)
now_create_folder = os.path.join(now_crate_path, 'Newfolder')
create_file = os.path.join(now_create_folder, "info.txt")
with open('info.txt', 'w') as x:
    x.write(f'This is My Crate Path {now_crate_path} and \n This my Now dir path {now_create_folder} and \n This is my file path {create_file}')
    x.close()

print('Program Run Successfull!')

