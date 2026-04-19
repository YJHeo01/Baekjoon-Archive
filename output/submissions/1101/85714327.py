import heapq

def main():
    card = [list(map(int,input().split())) for _ in range(n)]
    colorCntOfBox, cardCntOfColor = [0] * n, [0] * m
    answer = 0
    init(card,colorCntOfBox,cardCntOfColor)
    q = []
    for i in range(n):
        heapq.heappush(q,(-colorCntOfBox[i],i))
    tmp, idx = heapq.heappop(q)
    for j in range(m):
        if card[idx][j] != 0:
            cardCntOfColor[j] -= 1
    while q:
        tmp, idx = heapq.heappop(q)
        if tmp == -1 and max(cardCntOfColor) <= 1: break
        no_counting = False
        for j in range(m):
            if card[idx][j] != 0:
                if tmp == -1 and cardCntOfColor[j] == 1: no_counting = True
                cardCntOfColor[j] -= 1
        answer += 1
        if no_counting: answer -= 1
    print(answer)

def init(card,colorCntOfBox,cardCntOfColor):
    for i in range(n):
        for j in range(m):
            if card[i][j] == 0: continue
            colorCntOfBox[i] += 1
            cardCntOfColor[j] += 1

if __name__ == "__main__":
    n,m = map(int,input().split())
    main()