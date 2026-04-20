#define min(x,y) (x < y)? x : y

#include <stdio.h>

int num[100000] = { 0, };
int sorted[100000] = { 0, };
void merge(int left, int mid, int right) {
	int i = left, j = mid + 1, k = left;
	while (i <= mid && j <= right) {
		if (num[i] < num[j]) {
			sorted[k++] = num[i++];
		}
		else {
			sorted[k++] = num[j++];
		}
	}
	while (i <= mid) {
		sorted[k++] = num[i++];
	}

	while (j <= right) {
		sorted[k++] = num[j++];
	}
	for (int i = left; i <= right; i++) {
		num[i] = sorted[i];
	}
}
void merge_sort(int left, int right) {
	if (left < right) {
		int mid = (left + right) / 2;
		merge_sort(left, mid);
		merge_sort(mid+1, right);
		merge(left, mid, right);
	}
}
void main(void) {
	int n, m;
	int answer = 2000000000;
	scanf("%d %d", &n, &m);
	for (int i = 0; i < n; i++) {
		scanf("%d", &num[i]);
	}
	merge_sort(0, n - 1);
	int left = 0, right = 1;
	while (right < n) {
		if (num[right] - num[left]>=m) {
			answer = min(answer, num[right] - num[left]);
			left++;
		}
		else {
			right++;
		}
	}
	printf("%d", answer);
}