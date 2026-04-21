#include <stdio.h>
#include <stdlib.h>
int k=0, answer = -1;
int cnt = 0;
int list[500000] = { 0 };
int sorted[500000] = { 0 };
void merge(int left, int mid, int right) {
	int i = left, j = mid + 1, m = left;
	while (i <= mid && j <= right) {
		if (list[i] <= list[j]) {
			sorted[m++] = list[i++];
		}
		else {
			sorted[m++] = list[j++];
		}
	}
	while (i <= mid) {
		sorted[m++] = list[i++];
	}
	while (j <= right) {
		sorted[m++] = list[j++];
	}
	for (int a = left; a <= right; a++) {
		cnt++;
		list[a] = sorted[a];
		if (cnt == k) {
			answer = list[a];
		}
	}
}
void merge_sort(int left, int right) {
	if (left < right) {
		int mid = (left + right) / 2;
		merge_sort(left, mid);
		merge_sort(mid + 1, right);
		merge(left, mid, right);
	}
}
int main() {
	int n = 0;
	scanf("%d %d", &n, &k);
	for (int i = 0; i < n; i++) {
		scanf("%d", &list[i]);
	}
	merge_sort(0, n-1);
	printf("%d\n", answer);
}