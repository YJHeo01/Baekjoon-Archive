#include <stdio.h>

int dp[500][500] = { 0, };
int map[500][500] = { 0, };
int m, n;

int dfs(int x, int y) {
	if (x == m - 1 && y == n - 1) {
		return 1;
	}
	int dx[4] = { 0,1,0,-1 };
	int dy[4] = { 1,0,-1,0 };
	for (int i = 0; i < 4; i++) {
		int nx = x + dx[i];
		int ny = y + dy[i];
		if (nx < 0 || ny < 0 || nx >= m || ny >= n || map[x][y] <= map[nx][ny]) {
			continue;
		}
		if (dp[nx][ny] != 0) {
			dp[x][y] += dp[nx][ny];
		}
		else {
			dp[x][y] += dfs(nx, ny);
		}
	}
	return dp[x][y];
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