def main():
    n,k = map(int,input().split())
    array = [0] + sorted(list(map(int,input().split())))
    distance_list = []
    answer = 0
    for i in range(n):
        distance = array[i+1] - array[i]
        answer += distance
        distance_list.append(distance)
    distance_list.sort()
    for _ in range(k):
        answer -= distance_list.pop()
    print(answer)

if __name__ == "__main__":
    main()