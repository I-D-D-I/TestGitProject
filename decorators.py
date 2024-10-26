def uppercase(func):
    def wrapper():
        return func().upper()

    return wrapper

def braces(func):
    def wrapper():
        return '{' + func() + '}'

    return wrapper

def square_brackets(func):
    def wrapper():
        return '[' + func() + ']'

    return wrapper


@square_brackets
@uppercase
@braces
def greet():
    return 'Hello'

print(greet())