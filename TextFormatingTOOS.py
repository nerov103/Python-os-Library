
simple = ''';!@#$%)^&*<.>"/?:|,}'''
user_input = input('enter str> ')


stn  = ''
for i in user_input:
    if i not in simple:
        stn = stn + i

print(stn)



#Cretor Nerov Ahmead


