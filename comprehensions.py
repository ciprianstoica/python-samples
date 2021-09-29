
l = [x ** 2 for x in range(0, 10, 2)]
print(l)

s = {x * 2 for x in list('abcde')}
print(s)

t = tuple(10 / x for x in range(50, 30, -3) if x % 2 == 1)
print(t)

d = {x : 10 / x for x in range(50, 30, -3) if x % 2 == 1}
print(d)

s = [x.strip() for x in ['abc\n', '\n', 'cde\n', '\n', 'def\n'] if x.strip() != '']
print(s)

data = {x: 'par' if x % 2 == 0 else 'impar' for x in range(10)}

# leap year
leap_years = [x for x in range(2018, 2500) if x % 4 == 0 and x % 100 != 0 or x % 400 == 0]
print (leap_years)