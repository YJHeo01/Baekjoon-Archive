INF = 1000000

n = int(input())

array = list(map(int,input().split()))

balloon = [[] for _ in range(INF+1)]

for i in range(n): balloon[array[i]].append(i)
    
answer = 0

for high in range(INF,0,-1):
    while balloon[high]:
        answer += 1
        x = balloon[high].pop()
        while True:
            high -= 1
            if balloon[high] == [] or balloon[high][-1] <= x: break
            x = balloon[high].pop()

print(answer)