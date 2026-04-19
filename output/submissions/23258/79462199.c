#define MIN(a,b) ((a)<(b)?(a):(b))

#define SIZE 301
#define INF 1000000000

#include <stdio.h>

int time[301][301][301] = { 0, };
int main() {
	int n, q;
	scanf("%d %d", &n, &q);
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			scanf("%d", &time[0][i][j]);
			if (time[0][i][j] == 0) {
				time[0][i][j] = INF;
			}
		}
	}
	for (int c = 1; c <= n; c++) {
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				time[c][i][j] = time[c - 1][i][j];
			}
		}
		for (int k = 1; k < c; k++) {
			for (int i = 1; i <= n; i++) {
				for (int j = 1; j <= n; j++) {
					time[c][i][j] = MIN(time[c][i][j], time[c][i][k] + time[c][k][j]);
				}
			}
		}
	}
	for (int i = 0; i < q; i++) {
		int cc, s, e;
		scanf("%d %d %d", &cc, &s, &e);
		int answer = time[cc][s][e];
		if (answer >= INF) {
			answer = -1;
		}
		printf("%d\n", answer);
	}
}