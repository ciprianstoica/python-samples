
def factorial(n: int) -> int:
    if n == 1:
        return 1
    else:
        return factorial(n - 1) * n

print(factorial(5))

def tobinary(n: int):
    c = n // 2
    r = n % 2
    if c == 0:
        return str(r)
    else:
        return tobinary(c) + str(r)

print(tobinary(112))
