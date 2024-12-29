# fibonacci series

fib = [0,1]
# Range start from zero by default
for i in range(5):
    fib.append(fib[-1] + fib[-2])

# converting a list of integer

print(', '.join(str(e) for e in fib))