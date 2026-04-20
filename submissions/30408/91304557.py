n,m = map(int,input().split())

visited = set()

def f(visited,i):
    if i == 1:
        visited.add(i)
        return
    if i // 2 not in visited:
        visited.add(i//2)
        f(visited,i//2)
    if i % 2 == 1 and i // 2 + 1 not in visited:
        visited.add(i//2+1)
        f(visited,i//2+1)

f(visited,n)

if m in visited:
    print("YES")
else:
    print("NO")
