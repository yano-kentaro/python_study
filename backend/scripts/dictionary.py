dict = {
    "x": 1,
    "y": 2,
}
dict['x'] = 'test'
dict['z'] = 3

print('==================== 実行結果 ====================', end='\n\n')
print(f'dict = {dict}', type(dict), end='\n\n')
print(f'dict.keys() = {dict.keys()}', type(dict.keys()), end='\n\n')
print(f'dict.values() = {dict.values()}', type(dict.values()), end='\n\n')
