# using generator

def fibonacci(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

n = 10

print(list(fibonacci(n)))

# without using yield
def fibonacci_list(n):
    a, b = 0, 1
    result = []
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

print(fibonacci_list(10))
