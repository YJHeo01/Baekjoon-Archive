#include <stdio.h>

int n, m;
char banner[250][250] = { 0, };
char visited[250][250] = { 0, };

void dfs(int i, int j) {
	if (visited[i][j] == 1 || banner[i][j] == '0') {
		return;
	}
	visited[i][j] = 1;
	if (i >= 1) {
		dfs(i - 1, j);
	}
	if (j >= 1) {
		dfs(i, j - 1);
	}
	if (i < m - 1) {
		dfs(i + 1, j);
	}
	if (j < n - 1) {
		dfs(i, j + 1);
	}
	return;
}
int main() {
	scanf("%d %d", &m, &n);
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			scanf("%c", &banner[i][j]);
		}
	}
	int answer = 0;
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			if (banner[i][j] == '1' && visited[i][j] == 0) {
				dfs(i, j);
				answer += 1;
			}
		}
	}
	printf("%d", answer);
}