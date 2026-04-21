def main():
    n = int(input())
    graph = {}
    for _ in range(n):
        left, iis, right = input().split()
        if left not in graph:
            graph[left] = [right]
        else:
            graph[left].append(right)
        if right not in graph:
            graph[right] = []
    m = int(input())
    for _ in range(m):
        start, iis, target = input().split()
        if left not in graph or right not in graph:
            print("F")
            continue
        if solution(graph,start,target) == True:
            print("T")
        else:
            print("F")

def solution(graph,vx,target):
    if vx == target: return True
    ret_value = False
    for nx in graph[vx]:
        ret_value = ret_value or solution(graph,nx,target)
    return ret_value
    
if __name__ == "__main__":
    main()