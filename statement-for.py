
l = ['a', 'b', 'c']
t = ('d', 'e', 'f')

for x in l:
    print(x, end=' ')
else:
    print('Done')

for x in t:
    print(x, end=' ')
else:
    print('Done')


######################################

sum = 0
for x in range(5, 11, 2):
    sum += x
    print(x)
else:
    print(sum)

#######################################

for x in range(20, 6, -2):
    print(x)

######################################

for (x, y) in [(1,2), (3,4), (5,6)]:
    print(x, y)

######################################

s = {'a', 'b', 'c', 'a'}
d = {'d':2, 'e':3, 'f':8, 'e':9}

for x in s:
    print(x, end=' ')
else:
    print('Done')

for x in d:
    print(x, d[x], end=' ')
else:
    print('Done')


