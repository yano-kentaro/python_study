set = {1, 1, 1, 3, 4, 5}
set_2 = {1, 2, 3}
set_3 = set - set_2
set_4 = set_2 - set
set_5 = set_2 & set
set_6 = set_2 | set
set_7 = set_2 ^ set

print('==================== 実行結果 ====================', end='\n\n')
print(f'set = {set}', type(set), end='\n\n')
print(f'set_2 = {set_2}', type(set_2), end='\n\n')
print(f'set_3 = {set_3}', type(set_3), end='\n\n')
print(f'set_4 = {set_4}', type(set_4), end='\n\n')
print(f'set_5 = {set_5}', type(set_5), end='\n\n')
print(f'set_6 = {set_6}', type(set_6), end='\n\n')
print(f'set_7 = {set_7}', type(set_7), end='\n\n')
