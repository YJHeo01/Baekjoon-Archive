def main():
    cnt = 0
    answer = 0
    for _ in range(20):
        name, score, grade = input().split()
        if grade == 'P': continue
        score = float(score)
        cnt += score
        if grade == 'F': continue
        if grade[0] == 'A':
            answer += 4 * score
        elif grade[0] == 'B':
            answer += 3 * score
        elif grade[0] == 'C':
            answer += 2 * score
        else:
            answer += 1 * score
        if grade[1] == '+':
            answer += 0.5 * score
    print(answer/cnt)

if __name__ == "__main__":
    main()