def main():
    s = input()
    global length
    length = len(s)
    visited = [False] * length
    solution(s,visited,-1,0)

def solution(s,visited,cur_idx,alphabet):
    for next_alphabet in range(alphabet,26):
        for next_idx in range(cur_idx+1,length):
            if visited[next_idx]: continue
            if ord(s[next_idx]) - ord('A') == next_alphabet:
                visited[next_idx] = True
                for i in range(length):
                    if visited[i]: print(s[i],end="")
                print()
                solution(s,visited,next_idx,next_alphabet)
                
if __name__ == "__main__":
    main()