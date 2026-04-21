answer = 0
color = {"black":0,"brown":1,"red":2,"orange":3,"yellow":4,"green":5,"blue":6,"violet":7,"grey":8,"white":9}
for _ in range(2):
    answer *= 10
    answer += color[input()]
answer *= 10 ** color[input()]
print(answer)