tuple = (1, 2, 3, 4, 5)
tuple_2 = 6, 7, 8, 9, 10
tuple_1_2 = (tuple, tuple_2)
tuple_3 = tuple + tuple_2

print('==================== 実行結果 ====================', end='\n\n')
print(f'tuple = {tuple}', type(tuple), end='\n\n')
print(f'tuple_2 = {tuple_2}', type(tuple_2), end='\n\n')
print(f'tuple_1_2 = {tuple_1_2}', type(tuple_1_2), end='\n\n')
print(f'tuple_3 = {tuple_3}', type(tuple_3), end='\n\n')
