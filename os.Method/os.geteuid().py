# Python program to explain os.umask() method 
	
# importing os module 
import os 

# mask 
# 18 in decimal is 
# equal to 0o022 in octal 
mask = 18

# Set the current umask value 
# and get the previous 
# umask value 
umask = os.umask(mask) 


# Print the 
# current and previous 
# umask value 
print("Current umask:", mask) 
print("Previous umask:", umask) 
