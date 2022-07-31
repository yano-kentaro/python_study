def add_num(num1: int, num2: int) -> int | str:
    """引数num1とnum2を足した結果を返す関数
    Args:
        num1: int
        num2: int
    Returns:
        int | str
    """
    try:
        return num1 + num2
    except Exception as e:
        return f'Error: {e}'


print(add_num(1, 2))
print(add_num('1', '2'))
print(add_num(1, '2'))


def outer_func():
    def inner_func():
        print('inner_func')
    inner_func()


outer_func()
