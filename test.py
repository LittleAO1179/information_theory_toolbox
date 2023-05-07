a = input()
a1 = list(a)
a2 = set(a1)
for i in a2:
    print(f'{i}出现了{a1.count(i)}次')