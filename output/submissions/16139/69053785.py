import sys

input = sys.stdin.readline

s = list(input().rstrip())

l = len(s)

sentence = []
tmp = [0] * 26

q = int(input())

for i in s:
    tmp[ord(i)-ord('a')] += 1
    tmp_ = tmp.copy()
    sentence.append(tmp_)
for i in range(q):
    answer = 0
    a,b,c = input().strip().split()
    if a == s[int(b)]: #20번째 줄의 연산은 문장 s의 b번째 글자를 반영하지 못한다.
        answer += 1
    a = ord(a) - ord('a')
    answer += sentence[int(c)][a]-sentence[int(b)][a]
    print(answer)