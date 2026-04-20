#include <stdio.h>
int n = 0;

int find_max_idx(int A[], int start, int end) {
	int max_idx = start;
	for (int i = start; i <= end; i++) {
		if (A[i] > A[max_idx]) {
			max_idx = i;
		}
	}
	return max_idx;
}

void bubble_sort(int A[], int start, int end) {
	int tmp;
	for (int i = start; i > end; i--) {
		tmp = A[i];
		A[i] = A[i - 1];
		A[i - 1] = tmp;
	}
	return;
}

int sort(int A[], int start, int end) {
	if (end >= n) {
		end = n - 1;
	}
	int max_idx = find_max_idx(A, start, end);
	bubble_sort(A, max_idx, start);
	return max_idx - start;
}
int main() {
	int A_array[50] = { 0, };
	scanf("%d", &n);
	int s;
	for (int i = 0; i < n; i++) {
		scanf("%d ", &A_array[i]);
	}
	scanf("%d", &s);

	for (int i = 0; i < n; i++) {
		s -= sort(A_array, i, i+s);
		if (s <= 0) {
			break;
		}
	}
	for (int i = 0; i < n; i++) {
		printf("%d ", A_array[i]);
	}
	return 0;
}