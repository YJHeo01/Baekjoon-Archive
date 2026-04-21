#define MAX(a,b) a > b ? a : b
#include <stdio.h>

int n;
int solution(int board[][10], int bishop[][10], int x, int y, int bishop_cnt);
int get_nx(int x, int y);
int get_ny(int y);
int possible_make_new_bishop(int bishop[][10], int x, int y);

int main() {
	int board[10][10] = { 0, };
	int bishop[10][10] = { 0, };
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			scanf("%d", &board[i][j]);
		}
	}
	int answer = 0;
	answer = solution(board, bishop, 0, 0, 0);
	printf("%d", answer);
}

int solution(int board[][10], int bishop[][10], int x, int y, int bishop_cnt) {
	if (x == n) {
		return bishop_cnt;
	}
	int nx = get_nx(x, y);
	int ny = get_ny(y);
	int ret_value = solution(board, bishop, nx, ny, bishop_cnt);
	if (board[x][y] == 1 && possible_make_new_bishop(bishop, x, y) == 1) {
		bishop[x][y] = 1;
		ret_value = MAX(ret_value, solution(board, bishop, nx, ny, bishop_cnt+1));
		bishop[x][y] = 0;
	}
	return ret_value;
}

int get_nx(int x, int y) {
	if (y == n - 1) {
		return x + 1;
	}
	else {
		return x;
	}
}

int get_ny(int y) {
	if (y == n - 1) {
		return 0;
	}
	else {
		return y + 1;
	}
}

int possible_make_new_bishop(int bishop[][10], int x, int y) {
	int dx = -1;
	int dy[2] = { -1,1 };
	for (int i = 0; i < 2; i++) {
		int nx = x;
		int ny = y;
		while (1) {
			nx += dx;
			ny += dy[i];
			if (nx < 0 || ny < 0 || nx >= n || ny >= n) {
				break;
			}
			if (bishop[nx][ny] == 1) {
				return 0;
			}
		}
	}
	return 1;
}