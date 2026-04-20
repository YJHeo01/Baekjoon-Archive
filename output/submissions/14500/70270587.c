#define MAX(A,B) A > B ? A : B 
#define SUM(A,B,C,D) A+B+C+D
#include <stdio.h>

int paper[502][502] = { 0, };

int n, m; // n은 세로, m은 가로

int case1(int r, int c){
	int ret_value = SUM(paper[r][c], paper[r + 1][c], paper[r + 1][c + 1], paper[r][c + 1]);
	return ret_value;
}

int case2(int r, int c) {
	int ret_value = SUM(paper[r][c], paper[r + 1][c], paper[r + 1][c + 1], paper[r + 2][c + 1]);
	return ret_value;
}

int case3(int r, int c) {
	int ret_value = SUM(paper[r][c+1], paper[r + 1][c], paper[r + 1][c + 1], paper[r][c + 2]);
	return ret_value;
}

int case4(int r, int c) {
	int ret_value = SUM(paper[r][c + 1], paper[r + 1][c], paper[r + 1][c + 1], paper[r + 2][c]);
	return ret_value;
}

int case5(int r, int c) {
	int ret_value = SUM(paper[r][c], paper[r][c+1], paper[r][c + 2], paper[r][c + 3]);
	return ret_value;
}

int case6(int r, int c) {
	int ret_value = SUM(paper[r][c], paper[r + 1][c], paper[r + 2][c], paper[r + 3][c]);
	return ret_value;
}

int case7(int r, int c) {
	int ret_value = SUM(paper[r][c], paper[r][c+1], paper[r + 1][c + 1], paper[r + 1][c + 2]);
	return ret_value;
}

int case8(int r, int c) {
	int ret_value = SUM(paper[r][c], paper[r + 1][c], paper[r + 1][c + 1], paper[r + 1][c + 2]);
	return ret_value;
}

int case9(int r, int c) {
	int ret_value = SUM(paper[r][c], paper[r + 1][c], paper[r][c + 1], paper[r + 2][c]);
	return ret_value;
}

int case10(int r, int c) {
	int ret_value = SUM(paper[r][c], paper[r][c+1], paper[r][c + 2], paper[r + 1][c + 2]);
	return ret_value;
}

int case11(int r, int c) {
	int ret_value = SUM(paper[r+2][c], paper[r][c+1], paper[r + 1][c + 1], paper[r + 2][c + 1]);
	return ret_value;
}

int case12(int r, int c) {
	int ret_value = SUM(paper[r][c], paper[r + 1][c], paper[r][c + 1], paper[r][c + 2]);
	return ret_value;
}

int case13(int r, int c) {
	int ret_value = SUM(paper[r][c], paper[r + 1][c], paper[r + 2][c], paper[r + 2][c + 1]);
	return ret_value;
}

int case14(int r, int c) {
	int ret_value = SUM(paper[r][c + 2], paper[r + 1][c], paper[r + 1][c + 1], paper[r + 1][c + 2]);
	return ret_value;
}

int case15(int r, int c) {
	int ret_value = SUM(paper[r][c], paper[r][c+1], paper[r + 1][c + 1], paper[r + 2][c + 1]);
	return ret_value;
}

int case16(int r, int c) {
	int ret_value = SUM(paper[r][c + 1], paper[r + 1][c], paper[r + 1][c + 1], paper[r + 2][c + 1]);
	return ret_value;
}

int case17(int r, int c) {
	int ret_value = SUM(paper[r][c], paper[r + 1][c], paper[r + 1][c + 1], paper[r + 2][c]);
	return ret_value;
}

int case18(int r, int c) {
	int ret_value = SUM(paper[r][c + 1], paper[r + 1][c], paper[r + 1][c + 1], paper[r + 1][c + 2]);
	return ret_value;
}

int case19(int r, int c) {
	int ret_value = SUM(paper[r][c], paper[r][c+1], paper[r + 1][c + 1], paper[r][c + 2]);
	return ret_value;
}
int solution(int row, int column, int flag) {
	switch (flag)
	{
	case 1:
		return case1(row, column);
		break;
	case 2:
		return case2(row, column);
		break;
	case 3:
		return case3(row, column);
		break;
	case 4:
		return case4(row, column);
		break;
	case 5:
		return case5(row, column);
		break;
	case 6:
		return case6(row, column);
		break;
	case 7:
		return case7(row, column);
		break;
	case 8:
		return case8(row, column);
		break;
	case 9:
		return case9(row, column);
		break;
	case 10:
		return case10(row, column);
		break;
	case 11:
		return case11(row, column);
		break;
	case 12:
		return case12(row, column);
		break;
	case 13:
		return case13(row, column);
		break;
	case 14:
		return case14(row, column);
		break;
	case 15:
		return case15(row, column);
		break;
	case 16:
		return case16(row, column);
		break;
	case 17:
		return case17(row, column);
		break;
	case 18:
		return case18(row, column);
		break;
	case 19:
		return case19(row, column);
		break;

	default:
		break;
	}
}

int main() {

	scanf("%d %d", &n, &m);

	int answer = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			scanf("%d", &paper[i][j]);
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			for (int k = 1; k < 20; k++) {
				answer = MAX(solution(i, j, k), answer);
			}
		}
	}
	printf("%d", answer);
}