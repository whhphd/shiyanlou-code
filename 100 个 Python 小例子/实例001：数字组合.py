import itertools

sum1 = 0
for i, j, k in itertools.product(range(1, 5), repeat=3):
    if i != j and i != k and j != k:
        print(i, j, k)
        sum1 += 1

print('总数1：{}'.format(sum1))

sum2 = 0
for i in itertools.permutations(range(1, 5), 3):
    print(*i)
    sum2 += 1
print('总数2：{}'.format(sum2))
