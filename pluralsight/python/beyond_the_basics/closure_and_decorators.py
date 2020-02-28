def enclosing(x='closed over'):
    def local_function():
        print(x)

    return local_function


lf = enclosing()
lf()

lf2 = enclosing(x='other closed over')
lf2()
lf()

# Enclosing
print('-' * 15 + 'Enclosing' + '-' * 15)

message = 'global'


def enclosing():
    message = 'enclosing'

    def local():
        # global message
        # nonlocal message
        message = 'local'

    print('enclosing message:', message)
    local()
    print('enclosing message:', message)


print('global message:', message)
enclosing()
print('global message:', message)

# Decorators
print('-' * 15 + 'Decorators' + '-' * 15)


def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)

    return wrap


@escape_unicode
def northern_city():
    return 'Tromsø'


print(northern_city())
