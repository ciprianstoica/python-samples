
def func(a, b, c=9, d='asdf'):
    d.split()
    print("{} {} {} {}".format(a, b, c, d))


func(d = 'Nondefault', b = 1, c = 2, a = 3)

#############################################

def func(*args):
    for arg in args:
        print(arg)


func(23, 'ert', {'as': 123, 12: 34})

############################################


def func(**kwargs):
    print(kwargs)


func(b=23, c='ert', a=12)


###########################################

def func(*args, **kwargs):
    print(args)
    print(kwargs)


func('qwe', 45, b=23, c='ert', a=12)
