n, score, p = map(int,input().split())

if n == 0: ranking = 1
else:
    rank_list = list(map(int,input().split()))

    rank_list.sort(reverse=True)

    ranking = -1
    for i in range(n):
        if rank_list[i] <= score:
            ranking = i + 1
            break

    if n < p:
        if ranking == -1:
            ranking = n + 1
    elif score == rank_list[p-1]:
            ranking = -1        


    

print(ranking)