def main():
    cur_color = sorted(list(input()))
    target_color = sorted(list(input()))
    answer = 0
    for i in range(10):
        if cur_color[i] != target_color[i]:
            answer += 1
    print(answer)

if __name__ == "__main__":
    main()