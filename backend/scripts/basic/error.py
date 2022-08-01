print('==================== 実行結果 ====================', end='\n\n')

list = [1, 2, 3, 4, 5]


class OriginalError(Exception):
    pass


try:
    for i in range(5):
        print(list[i])
        list[i] = 'test'
except IndexError as e:
    print('IndexError:', e)
else:  # 例外が発生しなかった場合
    print('No error')
finally:  # 例外が発生しても、ここにくる
    print('finally')
    print('list =', list)

print('\n==================== 実行結果 ====================', end='\n\n')
