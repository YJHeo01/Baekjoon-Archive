n = int(input())
hash_table = [[] for _ in range(1000)]

card = list(map(int,input().split()))
m = int(input())
sang_keun_card = list(map(int,input().split()))

for i in card:
    idx = i % 1000
    hash_table[idx].append(i)

for j in sang_keun_card:
    idx = j % 1000
    if j not in hash_table[idx]:
        print("0",end=' ')
    else:
        print("1",end=' ')