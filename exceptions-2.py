
'''
Exception
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
'''

def get_val(x, i):
    print(x[i])


try:
    #get_val(['a', 'b'], 1)              # valid code
    # get_val(['a', 'b'], 3)              # IndexError: list index out of range
    ['a', 'b'][3]
    #get_val(5, 2)                       # TypeError: 'int' object is not subscriptable
    #get_val({'a': 123, 'b': 567}, 'c')  # KeyError: 'c'
except LookupError as ex:
    print(type(ex), ex)
except IndexError:
    print('IndexError caught')
except (IndexError, KeyError) as ex:
    print(type(ex), ex)
except Exception as ex:
    print(type(ex), ex)
else:
    print("No exception caught!")
finally:
    print("Finally...")

print("Done!")
