#include <stdio.h>

int A[1000001] = { 0 };

int main() {
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &A[i]);
	}
	int NGE = -1;
	for (int i = 0; i < n; i++) {
		for (int j = i+1; j < n; j++) {
			if (A[i] < A[j]) {
				NGE = A[j];
				break;
			}
		}
		printf("%d ", NGE);
		NGE = -1;
	}
}