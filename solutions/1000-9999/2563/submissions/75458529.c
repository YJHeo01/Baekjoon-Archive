#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool black_area[100][100] = { 0, };

int get_area_size(int x, int y) {
	int ret_value = 0;
	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < 10; j++) {
			int nx = x + i;
			int ny = y + j;
			if (black_area[nx][ny] == false) {
				black_area[nx][ny] = true;
				ret_value++;
			}
		}
	}
	return ret_value;
}
int main() {
	int n;
	scanf("%d", &n);
	int answer = 0;
	for (int i = 0; i < n; i++) {
		int a, b;
		scanf("%d %d", &a, &b);
		answer += get_area_size(a, b);
	}
	printf("%d", answer);
}