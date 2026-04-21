#include <iostream>
#include <vector>
#include <queue>

using namespace std;
int solution(vector<vector<int>> graph, int size);
void bfs(vector<vector<int>> graph, vector<vector<bool>>& visited, pair<int, int> start, int size, int high);

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL);
	
	int n;
	cin >> n;
	vector<vector<int>> ground(n, vector<int>(n));
	
	for (int i = 0;i < n;i++) {
		for (int j = 0;j < n;j++) {
			int tmp;
			cin >> tmp;
			ground[i][j] = tmp;
		}
	}

	int answer = solution(ground, n);

	cout << answer;

	return 0;
}

int solution(vector<vector<int>> graph, int size) {
	int ret_value = 0;
	
	for (int high = 0;high < 100;high++) {
		int area_cnt = 0;
		vector <vector<bool>> visited(size, vector<bool>(size, false));
		for (int i = 0;i < size;i++) {
			for (int j = 0;j < size;j++) {
				if (graph[i][j] <= high or visited[i][j]) continue;
				bfs(graph, visited, { i,j }, size, high);
				area_cnt += 1;
			}
		}
		ret_value = max(ret_value, area_cnt);
	}
	
	return ret_value;
}

void bfs(vector<vector<int>> graph, vector<vector<bool>>& visited, pair<int, int> start, int size, int high) {
	queue<pair<int, int>> q;
	q.push(start);
	int dx[4] = { 0,1,0,-1 };
	int dy[4] = { -1,0,1,0 };
	
	while (!q.empty()) {
		int x = q.front().first;
		int y = q.front().second;
		q.pop();
		for (int i = 0;i < 4;i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (nx < 0 or ny < 0 or nx >= size or ny >= size) continue;
			if (visited[nx][ny] == false and graph[nx][ny] > high) {
				visited[nx][ny] = true;
				q.push({ nx,ny });
			}
		}
	}
}