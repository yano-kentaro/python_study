print('==================== 実行結果 ====================', end='\n\n')


def decorator(func):
    def wrapper(*args, **kwargs):
        print('start')
        print(f'func.__name__ = {func.__name__}',
              type(func.__name__), end='\n\n')
        print(f'args = {args}', type(args), end='\n\n')
        print(f'kwargs = {kwargs}', type(kwargs), end='\n\n')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper


@decorator
def add_num(a, b):
    return a + b


r = add_num(1, 2)
print(r)


@decorator
def mul_num(a, b):
    return a * b


r = mul_num(2, 3)
print(r)
