list_1 = [1, 2, 3, 4, 5]
list_2 = [6, 7, 8, 9, 10]
nested_list = [list_1, list_2]

list_1_ref = list_1
list_1_copy = list_1.copy()
list_1_ref[0] = 'test'
list_1[1] = 'test2'

print('==================== 実行結果 ====================', end='\n\n')

print(f'nested_list = {nested_list}', type(nested_list), end='\n\n')
print(f'list_1_ref = {list_1_ref}', type(list_1_ref), end='\n\n')
print(f'list_1_copy = {list_1_copy}', type(list_1_copy), end='\n\n')
