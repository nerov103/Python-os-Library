import os



dir_name = 'Geeksforkeeks'
scend_dir_name = 'Geeks'
peth = 'C:\\Users\\nibir\\Downloads\\test'

pts = os.path.join(peth, dir_name)
pts_1 = os.path.join(peth, scend_dir_name)

os.mkdir(pts)
os.mkdir(pts_1)


print(dir_name)
print(scend_dir_name)



