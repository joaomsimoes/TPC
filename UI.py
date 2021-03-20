from funcs import *

userlist = []

# User input - list size
size = int(input('Choose a list size: '))

# User inputs - integers for the list
while len(userlist) < size:
        x = int(input('Choose a number for the list: '))
        userlist.append(x)


#functions to calculate the biggest number and delete the smallests numbers in the list
list_big_number(userlist)

delete_small_num(userlist)