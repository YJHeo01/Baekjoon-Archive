#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
#include <map>

using namespace std;

int graph[100][100] = { 0, };
bool visited[100][100] = { false, };
int n, m, k;

int bfs(int x, int y) {
	int ret_value = 1;
	visited[x][y] = true;
	queue<pair<int, int>> q;
	q.push({ x, y });
	
	int dx[4] = { 0,1,0,-1 };
	int dy[4] = { 1,0,-1,0 };
	
	while (!q.empty()) {
		pair<int, int> pos = q.front();
		int vx = pos.first;
		int vy = pos.second;
		q.pop();
		for (int i = 0;i < 4;i++) {
			int nx = vx + dx[i];
			int ny = vy + dy[i];
			if (nx < 0 || ny < 0 || nx >= n || ny >= n || visited[nx][ny] || graph[nx][ny] == 1) continue;
			ret_value += 1;
			visited[nx][ny] = true;
			q.push({ nx, ny });
		}
	}

	return ret_value;
}
int main() {
	ios::sync_with_stdio(false); cin.tie(NULL);
	
	cin >> n >> m >> k;

	for (int i = 0;i < n;i++) {
		for (int j = 0;j < n;j++) {
			cin >> graph[i][j];
		}
	}
	
	int need = 0;

	for (int i = 0;i < n;i++) {
		for (int j = 0;j < n;j++) {
			if (visited[i][j] || graph[i][j] == 1) continue;
			int tmp = bfs(i, j);
			need += (tmp / k);
			if(tmp % k != 0) need++;
		}
	}

	if (need == 0 || need > m) cout << "IMPOSSIBLE";
	else cout << "POSSIBLE" << "\n" << m - need;

}