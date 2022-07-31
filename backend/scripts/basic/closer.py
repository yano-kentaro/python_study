def outer(a, b):
    def inner():
        return a + b

    return inner


print(f'outer(1,2) = {outer(1,2)}', type(outer(1, 2)), end='\n\n')

f = outer(1, 2)
r = f()
print(r)
