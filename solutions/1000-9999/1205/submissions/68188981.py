n, score, p = map(int,input().split())

if n == 0: ranking = 1
else:
    rank_list = list(map(int,input().split()))

    rank_list.sort(reverse=True)

    ranking = -1
    for i in range(min(n,p)):
        if rank_list[i] < score:
            ranking = i+1
            break
        elif rank_list[i] == score:
            if i < p-1:
                ranking = i+1
                break

print(ranking)