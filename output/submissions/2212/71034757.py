n = int(input())

k = int(input())

sensor = list(map(int,input().split()))

sensor.sort()

distance = [0] * (k-1)

answer = sensor[n-1] - sensor[0]

for i in range(n-1):
    if sensor[i+1] - sensor[i] > distance[-1]:
        distance.append(sensor[i+1]-sensor[i])
        distance.sort(reverse=True)
        distance.pop()

for d in distance:
    answer -= d

print(answer)