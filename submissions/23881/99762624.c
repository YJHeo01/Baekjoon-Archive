#include <stdio.h>

int arr[10000] = { 0, };

void swap(int a, int b) {
	int tmp = arr[a];
	arr[a] = arr[b];
	arr[b] = tmp;
}
int main() {
	int n, k;
	scanf("%d %d", &n, &k);
	for (int i = 0;i < n;i++) scanf("%d", &arr[i]);
	for (int last = n;last >= 1;last--) {
		int max_idx = 0;
		for (int i = 0;i < last;i++) {
			if (arr[i] > arr[max_idx]) max_idx = i;
		}
		if (last-1 != max_idx) {
			k--;
			if (k == 0) printf("%d %d", arr[last-1], arr[max_idx]);
			swap(last - 1, max_idx);
		}
	}
	if (k > 0) printf("-1");
}