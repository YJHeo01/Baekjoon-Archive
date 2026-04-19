#include <stdio.h>
#include <stdlib.h>

int _array[500][500] = { 0, };
int dp[500][500] = { 0, };
int m, n;
int dfs(int x, int y) {
	if (dp[x][y] != 0) {
		return dp[x][y];
	}
	int dx[4] = { 0,1,0,-1 };
	int dy[4] = { 1,0,-1,0 };
	for (int i = 0; i < 4; i++) {
		int nx = x + dx[i];
		int ny = y + dy[i];
		if (nx < 0 || ny < 0 || nx >= m || ny >= n) {
			continue;
		}
		if (_array[x][y] > _array[nx][ny]) {
			dp[x][y] += dfs(nx, ny);
		}
	}
	return dp[x][y];
}
int main() {
	scanf("%d %d", &m, &n);
	dp[m - 1][n - 1] = 1;
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			scanf("%d", &_array[i][j]);
		}
	}
	dfs(0, 0);
	int answer = dp[0][0];
	printf("%d", answer);
}