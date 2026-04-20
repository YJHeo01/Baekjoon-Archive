#include <iostream>

using namespace std;

int matrix[1000][1000] = { 0, };

int main(int argc, char **argv) {
	int n, m;
	scanf("%d %d", &n, &m);
	for (int i = 0;i < n;i++) {
		for (int j = 0;j < m;j++) {
			int tmp;
			scanf("%d", &matrix[i][j]);
		}
	}
	int row_max_idx[1000] = { 0, };
	int column_max_idx[1000] = { 0, };
	for (int i = 0;i < n;i++) {
		for (int j = 0;j < m;j++) {
			if (matrix[i][j] > matrix[i][row_max_idx[i]]) row_max_idx[i] = j;
			if (matrix[i][j] > matrix[column_max_idx[j]][j]) column_max_idx[j] = i;
		}
	}

	for (int i = 0;i < n;i++) matrix[i][row_max_idx[i]] = 0;
	for (int j = 0;j < m;j++) matrix[column_max_idx[j]][j] = 0;

	long long int answer = 0;
	for (int i = 0;i < n;i++) {
		for (int j = 0;j < m;j++) {
			answer += matrix[i][j];
		}
	}

	cout << answer;
}