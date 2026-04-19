chess = []
for _ in range(8):
    chess.append(list(input()))
answer = 0
for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0 and chess[i][j] != '.':
            answer += 1

print(answer)