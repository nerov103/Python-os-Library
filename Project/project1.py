import os

get = os.getcwd()
sorch_path = os.path.join(get, r'Project\all file')

print(os.listdir(sorch_path))

dresneson_path = os.path.join(get, r"Project\JastNow")
if not os.path.exists(dresneson_path):
    os.mkdir(dresneson_path)


all_path = list(os.walk(sorch_path))
for r, d, f in all_path:
    print(r,d,f)





print('promram Run in Successfully!')