#include <stdio.h>
#include <stdlib.h>

int dfs(int _array[], int visited[], int idx) {
	int next_idx = _array[idx];
	if (visited[next_idx] == 2) {
		visited[idx] = 1;
		return 1;
	}
	else if (visited[next_idx] == 1) {
		visited[idx] = -1;
		return -1;
	}
	else {
		visited[next_idx] = 1;
		int ret_value = dfs(_array, visited, next_idx);
		visited[idx] = ret_value;
		return ret_value;
	}
}
int main() {
	int _array[101] = { 0, };
	int n;
	scanf("%d", &n);
	for(int i=1;i<=n;i++){
		scanf("%d", &_array[i]);
	}
	int visited[101] = { 0, };
	for (int i = 1; i <= n; i++) {
		if (visited[i] > 0) {
			continue;
		}
		visited[i] = 2;
		dfs(_array, visited, i);
	}
	int answer = 0;
	for (int i = 1; i <= n; i++) {
		if (visited[i] == 1) {
			answer += 1;
		}
	}
	printf("%d\n", answer);
	for (int i = 1; i <= n; i++) {
		if (visited[i] == 1) {
			printf("%d\n", i);
		}
	}
}