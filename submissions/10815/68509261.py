n = int(input())
hash_table = [[] for _ in range(10000)]

card = list(map(int,input().split()))
m = int(input())
sang_keun_card = list(map(int,input().split()))

for i in card:
    idx = i % 10000
    hash_table[idx].append(i)

for j in sang_keun_card:
    idx = j % 10000
    if j in hash_table[idx]:
        print("1",end=' ')
    else:
        print("0",end=' ')