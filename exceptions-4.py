# run in command line 'python -O filename.py' to deactivate the asserts

my_set = {'a', 'b'}

assert 'a' in my_set, "The element a is not there"
assert 'c' in my_set, "The element c is not there"

print("done")
