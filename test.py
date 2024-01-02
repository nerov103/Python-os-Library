import os
import shutil

dir_name =  'large'

if not os.path.exists(f'.\\{dir_name}'):
    os.makedirs(f'.\\{dir_name}')
    print('Successfull Create!')
    for y in range(1, 1000):
        os.mkdir(f".\\{dir_name}\\Folder {y+1}")
else:
    os.path.exists(f'.\\{dir_name}')
    print(f'{dir_name} name is exists! Pleass Whit!')
    # pat = os.path.join(f'.\\{dir_name}', dir_name)
    shutil.rmtree(dir_name)    
    print(f'Successfull Dellet {dir_name} this file, and Try Agin!')

# for  i in range(1, 200):
#     os.mkdir(f"example\\file{i+1}")



