def is_greather_than_18(age=0):
    '''
    DOCSTRING: This function return True if the age is greather than 18
    INPUT: age
    OUTPUT: True/False
    '''
    if age > 18:
        return True
    else:
        return False

if is_greather_than_18(19):
    print('Es mayor que 18')

help(is_greather_than_18)
