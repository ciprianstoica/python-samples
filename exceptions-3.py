
class ElementAlreadyExists(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        #return "The element already exists.."
        return self.text


def add_element(s, elem):
    if elem in s:
        raise ElementAlreadyExists('Elementul exista')
    else:
        s.add(elem)


my_set = set()

#############################
# add_element(my_set, 'a')
# print(my_set)
# add_element(my_set, 'b')
# print(my_set)
# add_element(my_set, 'a')
# print(my_set)

############################

try:
    add_element(my_set, 'a')
    add_element(my_set, 'b')
    add_element(my_set, 'a')
except ElementAlreadyExists as ex:
    # do something here, log the error, etc..
    print(type(ex), ex)
    raise ElementAlreadyExists('alta exceptie')
    # raise any other exception
    raise IndexError

########################

my_exception = ElementAlreadyExists('ala bala')
raise my_exception

print('FINISH')