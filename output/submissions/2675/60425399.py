n = int(input())
for i in range(n):
    R, S = input().split()
    R = int(R)
    for j in range(len(S)):
        print(S[j]*R, end='')
    print()