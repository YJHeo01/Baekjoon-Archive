#define MAX(a,b) a > b ? a : b

#include <stdio.h>
#include <stdbool.h>

int n;
int init_board[20][20] = { 0, };
void get_init_board(int board[][20], int n);
int get_max_value(int board[][20]);
void get_new_board(int board[][20], int new_board[][20]);
void move_block(int board[][20], bool merged[][20], int start[], int direction);
void move_left(int board[][20]);
void move_right(int board[][20]);
void move_up(int board[][20]);
void move_down(int board[][20]);
void play_game(int board[][20], int command);
int dfs(int board[][20], int move_cnt);

int main() {
	scanf("%d", &n);
	get_init_board(init_board, n);
	int answer = 0;
	answer = dfs(init_board, 0);
	printf("%d", answer);
}

void get_init_board(int board[][20], int n) {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			scanf("%d", &board[i][j]);
		}
	}
}

int dfs(int board[][20], int move_cnt) {
	if (move_cnt == 5) {
		return get_max_value(board);
	}
	int ret_value = 0;
	for (int command = 0; command < 4; command++) {
		int new_board[20][20] = { 0, };
		get_new_board(board, new_board);
		play_game(new_board, command);
		ret_value = MAX(ret_value, dfs(new_board, move_cnt + 1));
	}
	return ret_value;
}

int get_max_value(int board[][20]) {
	int ret_value = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			ret_value = MAX(ret_value, board[i][j]);
		}
	}
	return ret_value;
}

void get_new_board(int board[][20], int new_board[][20]) {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			new_board[i][j] = board[i][j];
		}
	}
}

void play_game(int board[][20], int command) {
	switch (command)
	{
	case 0:
		move_left(board);
		break;
	case 1:
		move_right(board);
		break;
	case 2:
		move_up(board);
		break;
	default:
		move_down(board);
		break;
	}
	return;
}

void move_left(int board[][20]) {
	bool merged[20][20] = { 0, };
	for (int y = 0; y < n; y++) {
		for (int x = 0; x < n; x++) {
			if (board[x][y] == 0) continue;
			int start[2] = { x,y };
			move_block(board, merged, start, 0);
		}
	}
}
void move_right(int board[][20]) {
	bool merged[20][20] = { 0, };
	for (int y = n-1; y >= 0; y--) {
		for (int x = 0; x < n; x++) {
			if (board[x][y] == 0) continue;
			int start[2] = { x,y };
			move_block(board, merged, start, 1);
		}
	}
}
void move_up(int board[][20]) {
	bool merged[20][20] = { 0, };
	for (int x = 0; x < n; x++) {
		for (int y = 0; y < n; y++) {
			if (board[x][y] == 0) continue;
			int start[2] = { x,y };
			move_block(board, merged, start, 2);
		}
	}
}
void move_down(int board[][20]) {
	bool merged[20][20] = { 0, };
	for (int x = n-1; x >= 0; x--) {
		for (int y = 0; y < n; y++) {
			if (board[x][y] == 0) continue;
			int start[2] = { x,y };
			move_block(board, merged, start, 3);
		}
	}
}

void move_block(int board[][20], bool merged[][20], int start[], int direction) {
	int dx[4] = { 0,0,-1,1 };
	int dy[4] = { -1,1,0,0 };
	int vx = start[0]; int vy = start[1]; int nx = vx; int ny = vy;
	int block_value = board[vx][vy];
	board[vx][vy] = 0;
	while (1) {
		nx += dx[direction];
		ny += dy[direction];
		if (nx < 0 || ny < 0 || nx >= n || ny >= n || merged[nx][ny] == true) {
			board[vx][vy] = block_value;
			return;
		}
		else if (board[nx][ny] == block_value) {
			merged[nx][ny] = true;
			board[nx][ny] += block_value;
			return;
		}
		else if (board[nx][ny] != 0) {
			board[vx][vy] = block_value;
			return;
		}
		else {
			vx = nx; vy = ny;
		}
	}
}