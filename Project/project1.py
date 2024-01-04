import os

get_folder_path = os.getcwd()
get_folder = os.path.join(get_folder_path, "Project\\all file")


destenation_folder = os.path.join(get_folder_path, "Project\\Folder For csv")
if not os.path.exists(destenation_folder):
    os.makedirs(destenation_folder)

txt_folder = os.path.join(get_folder_path, "Project\\Folder For txt")
if not os.path.exists(txt_folder):
    os.makedirs(txt_folder)

jpg_folder = os.path.join(get_folder_path, "Project\\Folder For jpg")
if not os.path.exists(jpg_folder):
    os.makedirs(jpg_folder)



for r, d, f in os.walk(get_folder):
    for valu in f:
        file_excction = os.path.splitext(valu)
        if file_excction[-1] == ".csv":
            os.rename(os.path.join(r, valu), f"{destenation_folder}\\{valu}")
        
        if file_excction[-1] == ".txt":
            os.rename(os.path.join(r, valu), f"{txt_folder}\\{valu}")

        if file_excction[-1] == ".jpg":
            os.rename(os.path.join(r, valu), f"{jpg_folder}\\{valu}")








print('Your Program in Successfully run!')

