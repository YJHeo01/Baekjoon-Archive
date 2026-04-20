n = int(input())
hash_table = [[] for _ in range(100000)]

card = list(map(int,input().split()))
m = int(input())
sang_keun_card = list(map(int,input().split()))

for i in card:
    idx = i % 100000
    hash_table[idx].append(i)

for j in sang_keun_card:
    idx = j % 100000
    if j not in hash_table[idx]:
        print("0",end=' ')
    else:
        print("1",end=' ')