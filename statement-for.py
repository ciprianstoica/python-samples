s = [3, 6, 56, -4, 23, -12, 44]
s2 = [(2, 5), 'ab', [-4, 0.7], {'q', 'y'}]

for e in s:
    print(e)

for e in s:
    print(e)
else:
    print('Yes, there is else in Python..')

for i in range(len(s)):
    print(i, s[i])

for i in range(1, len(s), 2):
    print(i, s[i])

for i, e in enumerate(s, start=0):
    print(i, e)

for x, y in s2:
    print(x, y)