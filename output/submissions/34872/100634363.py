n = int(input())

one = [[True] * n for _ in range(3)]
two = [[True] * n for _ in range(3)]

answer = [0] * (3*n)

for i in range(3*n):
    for j in range(n):
        if one[i//n][j] and two[i%3][j]:
            answer[i] = j + 1
            one[i//n][j] = False
            two[i%3][j] = False
            break

print(*answer)