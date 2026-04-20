n = int(input())
data = [0]*n
data = list(map(int,input().split()))
big = max(data)
small = min(data)

print(small,big)