#include <stdio.h>
#include <stdlib.h>

int block_route[4][500][500] = { 0, };
int map[500][500] = { 0, };
int m, n;

int dfs(int x, int y, int d) {
	if (x == m - 1 && y == n - 1) {
		return 1;
	}
	int ret_value = 0;
	int dx[4] = { 0,1,0,-1 };
	int dy[4] = { 1,0,-1,0 };
	for (int i = 0; i < 4; i++) {
		int nx = x + dx[i];
		int ny = y + dy[i];
		if (nx < 0 || ny < 0 || nx >= m || ny >= n || map[x][y] <= map[nx][ny] || block_route[i][nx][ny] == 1) {
			continue;
		}
		int tmp = dfs(nx, ny, d);
		if (tmp == 0) {
			block_route[i][nx][ny] = 1;
		}
		ret_value += tmp;
	}
	return ret_value;
}

int main() {
	scanf("%d %d", &m, &n);
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			scanf("%d", &map[i][j]);
		}
	}
	int answer;
	answer = dfs(0, 0, 0);
	printf("%d", answer);
}