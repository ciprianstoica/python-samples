# transforms a number from base 10 to base 2

n = 16
m = n
s = ''

while True:
    c = n // 2
    r = n % 2
    s = str(r) + s
    if c == 0:
        break
    n = c

print(s, bin(m))

