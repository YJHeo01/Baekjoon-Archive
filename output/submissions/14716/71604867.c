#include <stdio.h>

int n, m;
char banner[250][250] = { 0, };
char visited[250][250] = { 0, };

void dfs(int i, int j) {
	visited[i][j] = 1;
	int dx[8] = { -1,0,1,-1,1,-1,0,1 };
	int dy[8] = { -1,-1,-1,0,0,1,1,1};
	for (int k = 0; k < 8; k++) {
		int nx = j + dx[k];
		int ny = i + dy[k];
		if (nx < 0 || ny < 0 || nx >= n || ny >= m) {
			continue;
		}
		if (banner[ny][nx] == '1' && visited[ny][nx] == 0) {
			dfs(ny, nx);
		}
	}
	return;
}
int main() {
	scanf("%d %d", &m, &n);
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			scanf("%c ", &banner[i][j]);
            visited[i][j] = 0;
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