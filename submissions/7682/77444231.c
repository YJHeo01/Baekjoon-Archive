#include <stdio.h>
#include <stdbool.h>

bool check_full_board(char board[][3]);
bool check_three_combo(char board[][3], char block_type);
int get_block_type_cnt(char board[][3], char block_type);
bool check_valid(char board[][3]);

int main() {
	while (true)
	{
		char board[10] = { 0, };
		scanf("%s", board);
		if (board[0] == 'e') {
			break;
		}
		bool valid = check_valid(board);
		if (valid == true) {
			printf("valid\n");
		}
		else
		{
			printf("invalid\n");
		}
	}
}

bool check_valid(char board[][3]) {
	int O_cnt = get_block_type_cnt(board,'O');
	int X_cnt = get_block_type_cnt(board,'X');
	if (O_cnt == X_cnt) {
		if (check_three_combo(board, 'O') == true && check_three_combo(board, 'X') == false) return true;
	}
	else if (O_cnt + 1 == X_cnt) {
		if (check_three_combo(board, 'O') == true) return false;
		if (check_three_combo(board, 'X') == true || check_full_board(board) == true) return true;
	}
	else return false;
	return false;
}

int get_block_type_cnt(char board[][3], char block_type) {
	int ret_value = 0;
	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			if (board[i][j] == block_type) {
				ret_value += 1;
			}
		}
	}
	return ret_value;
}

bool check_three_combo(char board[][3], char block_type) {
	for (int i = 0; i < 3; i++) {
		if (board[i][0] == block_type && board[i][1] == block_type && board[i][2] == block_type) return true;
		if (board[0][i] == block_type && board[1][i] == block_type && board[2][i] == block_type) return true;
	}
	if (board[0][0] == block_type && board[1][1] == block_type && board[2][2] == block_type) return true;
	if (board[2][0] == block_type && board[1][1] == block_type && board[0][2] == block_type) return true;
	return false;
}

bool check_full_board(char board[][3]) {
	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			if (board[i][j] == '.') return false;
		}
	}
	return true;
}