#define MIN(a,b) a > b ? b : a;
#define MAX(a,b) a > b ? a : b;
#include <stdio.h>

int graph[101][101] = {0,};
int area_item[101] = { 0, };

int main() {
	int n, m, r;

	scanf("%d %d %d", &n, &m, &r);
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			graph[i][j] = 999999;
		}
	}
	for (int i = 1; i <= n; i++) {
		scanf("%d ", &area_item[i]);
	}
	int a, b, l;
	for (int i = 0; i < r; i++) {
		scanf("%d %d %d", &a, &b, &l);
		graph[a][b] = l;
		graph[b][a] = l;
	}
	for (int k = 1; k <= n; k++) {
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				graph[i][j] = MIN(graph[i][j], graph[i][k] + graph[k][j]);
			}
		}
	}
	int answer = 0;
	for (int i = 1; i <= n; i++) {
		int tmp = area_item[i];
		for (int j = 1; j <= n; j++) {
			if (graph[i][j] <= m) {
				tmp += area_item[j];
			}
		}
		answer = MAX(answer, tmp);
	}
	printf("%d", answer);
}