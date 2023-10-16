# stored in tuple
def add(*args):
    print(args)
    print(type(args))
add(1,3,4,5,6,4)


# stored in dictionary format
def mul(**kwargs):
    print(kwargs)
    print(type(kwargs))
mul(name = "madhu", emp = 2991)