
x = 0
while True:
    x += 1
    if x % 2 == 1:
        continue
    if x > 30:
        break
    else:
        print(x)
else:
    print('This will never get printed')

###################################

x = 0
while x < 30:
    x += 1
    if x % 2 == 1:
        continue
    print(x)
else:
    print('This will get printed')
