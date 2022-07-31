print('==================== 実行結果 ====================', end='\n\n')

animal = 'cat'


def f():
    global animal
    animal = 'dog'
    print(f'animal = {animal}', type(animal), end='\n\n')


f()


print('\n==================== 実行結果 ====================', end='\n\n')
