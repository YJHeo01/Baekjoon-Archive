n = int(input())

shirts = list(map(int,input().split()))

t,p = map(int,input().split())

answer1 = 0

for shirt in shirts:
    answer1 += (shirt // (t+1) + 1)

print(answer1)
print(n//p, n%p)