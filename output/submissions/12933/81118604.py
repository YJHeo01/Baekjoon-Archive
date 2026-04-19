def main():
    s = list(input())
    length = len(s)
    visited = [False] * length
    idx = 0
    duck = ['q','u','a','c','k']
    answer = 0
    
    while True:
        finish = True
        for i in range(length):
            if visited[i] == False and s[i] == duck[idx]:
                visited[i] = True
                finish = False
                idx += 1
                if idx == 5:
                    idx = 0
        if finish: break
        if idx != 0:
            answer = -1
            break
        answer += 1
    print(answer)
            
if __name__ == "__main__":
    main()