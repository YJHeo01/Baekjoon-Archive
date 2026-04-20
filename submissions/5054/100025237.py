t = int(input())

for _ in range(t):
    input()
    a = list(map(int,input().split()))
    print(2*(max(a)-min(a)))