#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

char map[5][5] = { 0, };
bool visited[5][5] = { 0, };
int r, c, k;

int solution(int x, int y, int d) {
	if (d == k) {
		if(x == 0 && y == (c - 1)) {
			return 1;
		}
		else {
			return 0;
		}
	}
	int ret_value = 0;
	int dx[4] = { 0,1,0,-1 };
	int dy[4] = { 1,0,-1,0 };
	for (int i = 0; i < 4; i++) {
		int nx = x + dx[i];
		int ny = y + dy[i];
		if (nx < 0 || ny < 0 || nx >= r || ny >= c || map[nx][ny] == 'T' || visited[nx][ny] == true) {
			continue;
		}
		visited[nx][ny] = true;
		ret_value += solution(nx, ny, d + 1);
		visited[nx][ny] = false;
	}
	return ret_value;
}

int main() {
	scanf("%d %d %d", &r, &c, &k);
	for (int i = 0; i < r; i++) {
		scanf("%s", map[i]);
	}
	visited[r - 1][0] = true;
	int answer = solution(r-1,0,1);
	printf("%d", answer);
}