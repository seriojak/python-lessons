# Lambda
def first_name(name):
    """Get first name"""
    return name.splite()[0]


lambda_first_name = lambda name: name.splite()[0]

# Callable
print('-' * 15 + 'Callable' + '-' * 15)

print(callable(list))


class CallMe:
    def fake_def(self):
        pass


call_me = CallMe()

print(callable(call_me))


class CallMe:
    def __call__(self):
        print("Called!")

    def fake_def(self):
        pass


call_me = CallMe()

print("call_me:", callable(call_me))
call_me()

# Extended Arguments
print('-' * 15 + 'Extended Arguments' + '-' * 15)


def hyper_volume(*args):
    print("args:", args)
    print("type:", type(args))


hyper_volume(3, 4)


def tag(name, **kwargs):
    print("name:", name)
    print("kwargs:", kwargs)
    print("type:", type(kwargs))


tag('img', src="monet.jpg", alt="Sunrise by Claude Monet", border=1)
