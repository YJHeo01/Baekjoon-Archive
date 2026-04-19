#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int _array[100001] = { 0, };
bool visited[100001] = { 0, };

int dfs(int graph[], bool visited[], int start, int idx) {
	int nx = graph[idx];
	if (nx == start) {
		visited[idx] = true;
		return 0;
	}
	if (visited[nx] == true) {
		return 1;
	}
	visited[idx] = true;
	int ret_value = dfs(graph, visited, start, nx);
	if (ret_value == 1) {
		visited[idx] = false;
	}
	return ret_value;
}
int main() {
	int t;
	scanf("%d", &t);
	while (1) {
		if (t == 0) {
			break;
		}
		int answer = 0;
		t--;
		int n;
		scanf("%d", &n);
		for (int i = 1; i <= n; i++) {
			scanf("%d", &_array[i]);
		}
		for (int i = 1; i <= n; i++) {
			if (visited[i] == false) {
				answer += dfs(_array, visited, i, i);
				visited[i] = true;
			}
		}
		for (int i = 1; i <= n; i++) {
			visited[i] = false;
		}
		printf("%d\n", answer);
	}
}