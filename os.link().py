import os

# Source file path
src = 'C:\\Users\\nibir\\Downloads\\test\\Java\\file.txt'

# Destination file path
dst = 'C:\\Users\\nibir\\Downloads\\test\\Jsscript\\filex.txt'

# Create a hard link from the source to the destination
os.link(src, dst)

print("Hard link created successfully")






