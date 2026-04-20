import sys
input = sys.stdin.readline

def main():
    n,k = map(int,input().split())
    room = []
    answer = 0
    meet = sorted([list(map(int,input().split())) for _ in range(n)],key=lambda x:x[1])
    for start,end in meet:
        if len(room) < k:
            answer += 1
            room.append(end)
        else:
            room.sort(reverse=True)
            while room:
                tmp = room.pop()
                if tmp > start: 
                    room.append(tmp)
                    break
            if len(room) != k:
                answer += 1
                room.append(end)
    print(answer)

if __name__ == "__main__":
    main()