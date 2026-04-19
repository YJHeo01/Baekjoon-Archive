def main():
    s = list(input())
    length = len(s)
    visited = [False] * length
    idx = 0
    quack_visited = [0] * 5
    duck = ['q','u','a','c','k']
    answer = 0
    
    while True:
        correct = False
        for i in range(length):
            if visited[i] == False and s[i] == duck[idx]:
                visited[i] = True
                quack_visited[idx] = 1
                idx += 1
                if idx == 5:
                    idx = 0
                    correct = True
        if idx != 0:
            answer = -1
            break
        if correct == False:
            break
        answer += 1

    for i in range(length):
        if visited[i] == False:
            answer = -1
            break
    print(answer)
            
if __name__ == "__main__":
    main()