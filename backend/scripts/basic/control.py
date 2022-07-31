from tracemalloc import start


print('==================== 実行結果 ====================', end='\n\n')

x = 21

if x < 10:
    print('x < 10')
elif x < 20:
    print('x < 20')
else:
    print('x >= 20')

list = [1, 2, 3, 4, 5]
n = 1
m = 6

if n in list:
    print('n in list')

if m not in list:
    print('m not in list')

l = 0
if l:
    print('l is True')

is_empty = False
if is_empty is None:
    print('is_empty is True')

count = 5
while count:
    if count == 3:
        print('count == 3')
        break   # breakで抜けると、elseは実行されない
    print(count)
    count -= 1
else:
    print('count is 0')

# while True:
#     word = input('Enter a word: ')
#     if word == 'quit':
#         break
#     print(f'You entered: {word}')

for i in range(5):
    print(i)
    if i == 3:
        break

for i in range(2, 10, 4):
    print(i)

for fruit in enumerate(['apple', 'banana', 'orange']):
    print(fruit, type(fruit))

days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', 'Sunday']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)

print('==================== 実行結果 ====================', end='\n\n')
