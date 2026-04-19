def main():
    x,y = [],[]
    for _ in range(3):
        a,b = map(int,input().split())
        x.append(a); y.append(b)
    x.sort(); y.sort()
    answer_x, answer_y = 0,0
    if x[0] == x[1]: answer_x = x[2]
    else: answer_x = x[0]
    if y[0] == y[1]: answer_y = y[2]
    else: answer_y = y[0]
    print(answer_x,answer_y)

if __name__ == "__main__":
    main()