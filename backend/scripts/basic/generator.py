from os import sep


print('==================== 実行結果 ====================', end='\n\n')

l = ['Good Morning', 'Good Afternoon', 'Good Evening']

for i in range(len(l)):
    print(l[i])

print('\n#################################################', end='\n\n')


def greeting():
    yield 'Good Morning'
    yield 'Good Afternoon'
    yield 'Good Evening'


for i in greeting():
    print(i)

print('\n#################################################', end='\n\n')

g = greeting()
print(next(g))
print(next(g))
print(next(g))

print('\n##################################################', end='\n\n')


def counter(start_at=0):
    count = start_at
    while True:
        yield count
        count += 1


c = counter(10)
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
