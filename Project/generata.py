import os

now_get_path = os.getcwd()
sorch_path = os.path.join(now_get_path, "Project\\all file")

csv_file_len = 10
txt_file_len  = 10
jpg_file_len = 10




for i in range(1, csv_file_len):
    with open(f'{sorch_path}\\example{i+1}.txt', 'w') as f:
        f.write('Hello World!')
        f.close()

for i in range(1, txt_file_len):
    with open(f'{sorch_path}\\example{i+1}.jpg', 'w') as f:
        f.write('Hello World!')
        f.close()

for i in range(1, jpg_file_len):
    with open(f'{sorch_path}\\example{i+1}.csv', 'w') as f:
        f.write('Hello World!')
        f.close()





print('Program Success!')

