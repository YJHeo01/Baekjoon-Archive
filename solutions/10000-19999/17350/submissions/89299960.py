import sys

input = sys.stdin.readline

n = int(input())

answer = "뭐야?"

for _ in range(n):
    if(input().rstrip() == "anj"): answer = "뭐야;"
    
print(answer)