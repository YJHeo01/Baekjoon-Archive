def main():
    s = list(input())
    length = len(s)
    visited = [False] * length
    idx = 0
    duck = ['q','u','a','c','k']
    answer = 0
    while True:
        correct = False
        for i in range(length):
            if visited[i] == False and s[i] == duck[idx]:
                visited[i] = True
                idx += 1
                if idx == 5:
                    idx = 0
                    correct = True
        if correct == False:
            break
        answer += 1
    if answer == 0: answer = -1
    print(answer)
            
if __name__ == "__main__":
    main()