def main():
    n = int(input())
    answer = 0
    for _ in range(n):
        correct = True
        visited = [False] * 26
        s = input()
        last_c = ''
        for c in s:
            if last_c != c:
                if visited[ord(c)-ord('a')] == True:
                    correct = False
                    break
                visited[ord(c)-ord('a')] = True
                last_c = c
        if correct == True:
            answer += 1
    print(answer)
        
if __name__ == "__main__":
    main()