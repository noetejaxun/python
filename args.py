def myFunc(*args):
    return sum(args) * 0.05

print(myFunc(40, 60, 100, 1,34,122))

def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choise is {}'.format(kwargs['fruit']))
    else:
        print('I di not find any fruit here')

myfunc(fruit='apple', veggie = 'lettuce')


def myString(x):
    out = []
    for i in range(len(x)):
        if i%2==0:
            out.append(x[i].lower())
        else:
            out.append(x[i].upper())
    return ''.join(out)

print(myString('Hola, esta es una prueba'))
