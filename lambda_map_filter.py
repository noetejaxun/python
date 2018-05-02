#-----------------------------------#
# map function
#-----------------------------------#
#help(map)

def square(num):
    return num**2

my_nums = [1,2,3,4,5]

#print(map(square, my_nums))
for item in map(square, my_nums):
    print(item)

#-----------------------------------#
def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

names = ['Luis', 'Cristian', 'Leticia']

print(list(map(splicer, names)))

#-----------------------------------#
# Filter function
#-----------------------------------#

def check_even(num):
    return num%2 == 0

mynums = [1,2,3,4,5,6]

print(list(filter(check_even, mynums)))


square_2 = lambda num: num ** 2

print(square_2(3))

print(list(map(lambda first_letter: first_letter[0], names)))
