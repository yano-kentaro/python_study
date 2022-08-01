print('==================== 実行結果 ====================', end='\n\n')

s = "kvmfdklbjfdbndljfblnjfbsjfhbidfshlbuhssfbhzbvhjdbjvkfhdjvhzh"

d = {}
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)

d = {}
for i in s:
    d.setdefault(i, 0)
    d[i] += 1
print(d)

print('\n==================== 実行結果 ====================', end='\n\n')
