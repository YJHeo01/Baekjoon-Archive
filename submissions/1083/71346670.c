#include <stdio.h>


int n;

void sort(int A[]) {
	for (int j = 1; j < n; j++) {
		if (A[j - 1] < A[j]) {
			int tmp = A[j - 1];
			A[j - 1] = A[j];
			A[j] = tmp;
			break;
		}
	}
}

int main() {
	int A_array[50] = { 0, };
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d ", &A_array[i]);
	}
	int s;
	scanf("%d", &s);
	for (int i = 0; i < s; i++) {
		sort(A_array);
	}
	for (int i = 0; i < n; i++) {
		printf("%d ", A_array[i]);
	}
	return 0;
}