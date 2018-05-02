x = 25

def printer():
    x = 50
    return x

print(x)
print(printer())

# LEGB Rule:
# L: Local - names assigned in any away within a function (def or lambda) and not declared global in that function.
# E: Enclosing function locals - Names in the local scope of any and all enclosing functions (def or lambda), from inner to outer.
# G: Global (module) - Names assigned at the top.level of a module file, or declared global in a def within the file.
# B: Built-in (Python) - Names preassigned in the built-in names module: open, range, SyntaxError...

# GLOBAL
name = 'THIS IS A GLOBAL STRING'

def greet():
    # ENCLOSING
    name = 'THIS IS A ENCLOSING STRING'

    def hello():
        #LOCAL
        name = 'THIS IS A LOCAL STRING'
        print('Hello ' + name)
    hello()

greet()

help(len)
