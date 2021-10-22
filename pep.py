# Python Enhancement Proposals
# PEP 8 - https://www.python.org/dev/peps/pep-0008/
# import this

# correct all the 'errors' from below according to PEP 8

def getMaxNumber(my_param = 8, c = 9):
    if c<my_param :
        return 1
    else:
       return 2

def get_min_number():
      return 1

class myclass:
    def my_method(self):
        pass


    def my_method2(self):
        pass


L = getMaxNumber(5)

a = getMaxNumber(8); b = get_min_number()