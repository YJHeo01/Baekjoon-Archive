#include <stdio.h>

int arr[10000] = { 0, };

int a[10000] = { 0, };
int b[10000] = { 0, };

void swap(int x, int y) {
	int tmp = a[x];
	a[x] = a[y];
	a[y] = tmp;
}

void select_sort(int last) {
	int max_idx = 0;
	for (int i = 0;i <= last;i++) {
		if (a[i] > a[max_idx]) max_idx = i;
	}
	swap(max_idx, last);
}

int compare(int n) {
	for (int i = 0;i < n;i++) {
		if (a[i] != b[i]) return 0;
	}
	return 1;
}

int main() {
	int n;
	
	scanf("%d", &n);
	
	for (int i = 0;i < n;i++) scanf("%d", &a[i]);
	for (int i = 0;i < n;i++) scanf("%d", &b[i]);

	int answer = 0;
	for (int last = n - 1;last >= 1;last--) {
		select_sort(last);
		answer |= compare(n);
	}

	printf("%d", answer);
}