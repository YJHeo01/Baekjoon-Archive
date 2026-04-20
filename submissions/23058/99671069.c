#define min(a, b) (((a) < (b)) ? (a) : (b))

#include <stdio.h>

int board[10][10] = { 0, };
int n;

int check(int mask) {
	int row_flag[10] = { 0, };
	int column_flag[10] = { 0, };
	int ret_value = 0;
	for (int i = 0;i < n;i++) { 
		if ((1 << i) & mask) { row_flag[i] = 1; ret_value++; }
		if ((1 << (i + n)) & mask) { column_flag[i] = 1; ret_value++; }
	}
	
	for (int i = 0;i < n;i++) {
		for (int j = 0;j < n;j++) {
			int flag = row_flag[i] ^ column_flag[j];
			ret_value += (flag ^ board[i][j]);
		}
	}
	return ret_value;
}

int main() {
	scanf("%d", &n);
	for (int i = 0;i < n;i++) {
		for (int j = 0;j < n;j++) scanf("%d", &board[i][j]);
	}
	int answer = 100;
	for (int mask = 0;mask < (1 << (2 * n));mask++) answer = min(answer, check(mask));
	printf("%d", answer);
}