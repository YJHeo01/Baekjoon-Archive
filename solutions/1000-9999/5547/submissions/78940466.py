from collections import deque

def main():
	graph = init_graph(h)
	visited_building = [[False]*w for _ in range(h)]
	answer = 0
	for x in range(h):
		for y in range(w):
			if visited_building[x][y] == True or graph[x][y] == 0: continue
			answer += all_block_length(graph,visited_building,(x,y))
	visited_building = [[False]*w for _ in range(h)]
	for x in range(h):
		for y in range(w):
			if visited_building[x][y] == True or graph[x][y] == 1: continue
			answer -= inner_block_length(graph,visited_building,(x,y))
	print(answer)

def init_graph(h):
	graph = []
	for _ in range(h):
		graph.append(list(map(int,input().split())))
	return graph

def all_block_length(graph,visited,start):
	queue = deque([start])
	dx = [[1,1,0,-1,-1,0],[-1,0,1,1,0,-1]]
	dy = [[0,1,1,1,0,-1],[-1,-1,-1,0,1,0]]
	ret_value = 0
	visited[start[0]][start[1]] = True
	while queue:
		vx, vy = queue.popleft()
		tmp = vx % 2
		for i in range(6):
			nx = vx + dx[tmp][i]
			ny = vy + dy[tmp][i]
			if nx < 0 or ny < 0 or nx >= h or ny >= w or graph[nx][ny] == 0: ret_value += 1
			else:
				if visited[nx][ny] == True: continue
				visited[nx][ny] = True
				queue.append((nx,ny))
	return ret_value

def inner_block_length(graph,visited,start):
	queue = deque([start])
	dx = [[1,1,0,-1,-1,0],[-1,0,1,1,0,-1]]
	dy = [[0,1,1,1,0,-1],[-1,-1,-1,0,1,0]]
	visited[start[0]][start[1]] = True
	not_inner = False
	ret_value = 0
	while queue:
		vx,vy = queue.popleft()
		tmp = vx % 2
		for i in range(6):
			nx = vx + dx[tmp][i]
			ny = vy + dy[tmp][i]
			if nx < 0 or ny < 0 or nx >= h or ny >= w:
				not_inner = True
				continue
			if graph[nx][ny] == 1: ret_value += 1
			else:
				if visited[nx][ny] == True: continue
				visited[nx][ny] = True
				queue.append((nx,ny))
	if not_inner == True: ret_value = 0
	return ret_value
				
if __name__ == "__main__":
	w,h = map(int,input().split())
	main()