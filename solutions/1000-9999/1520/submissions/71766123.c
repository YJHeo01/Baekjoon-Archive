#include <stdio.h>

int graph[501][501] = { 0, };

int m, n;

int dfs(x, y) {
	if (x == n && y == m) {
		return 1;
	}
	int ret_value = 0;
	if ((x - 1 > 0) && (graph[y][x] > graph[y][x - 1])) {
		ret_value += dfs(x - 1, y);
	}
	if ((y - 1 > 0) && (graph[y][x] > graph[y - 1][x])) {
		ret_value += dfs(x, y - 1);
	}
	if ((x + 1 <= n) && (graph[y][x] > graph[y][x + 1])) {
		ret_value += dfs(x + 1, y);
	}
	if ((y + 1 <= m) && (graph[y][x] > graph[y + 1][x])) {
		ret_value += dfs(x, y + 1);
	}
	return ret_value;
}
int main() {
	scanf("%d %d", &m, &n);
	for (int i = 1; i <= m; i++) {
		for (int j = 1; j <= n; j++) {
			scanf("%d", &graph[i][j]);
		}
	}
	printf("%d", dfs(1, 1));
}