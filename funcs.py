"""
1.Create a .py file with two functions:
i.One that receives a list with numbers and returns the biggest.
ii.Other that receives a list of numbers and returns the same list without the smallest.
"""

def list_big_number(userlist):
    """ Receives a list with numbers and returns the biggest """

    print('The biggest value from the list is: ', max(userlist))


def delete_small_num(userlist):
    """ Receives a list of numbers and prints the same list without the smallest number """
    
    smallnumber = min(userlist)
    userlist_new = [x for x in userlist if x != min(userlist)]
    print('From the list it was removed the number: ', smallnumber, ' and your final list is: ', userlist_new)