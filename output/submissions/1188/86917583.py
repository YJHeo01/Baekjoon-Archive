n,m = map(int,input().split())

def euclidean(a,b):
    if b == 0: return a
    return euclidean(b,a%b)

cnt = n // euclidean(n,m) * m

answer = (cnt // n - 1) * n

if n <= m:
    answer = min(answer,(m-n)*n)

print(answer)