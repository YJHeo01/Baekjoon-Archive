s = list(input())
alpha = [-1]*26
for i in range(len(s)):
    tmp = ord(s[i]) - ord('a')
    if alpha[tmp] == -1:
        alpha[tmp] = i

for i in range(26):
    print(alpha[i], end=' ')