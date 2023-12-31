import os

# Open a directory using os.open()
fd = os.open("/", os.O_RDONLY)  # Open "/tmp" directory with read-only access

# Change the current working directory to the opened directory
os.fchdir(fd)

# Verify the change
print("Current working directory:", os.getcwd())

# Close the directory descriptor
os.close(fd)






