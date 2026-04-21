#define _CRT_SECURE_NO_WARNINGS
#define MIN(a,b) a > b ? b : a
#define MAX(a,b) a > b ? a : b
#define INF 2000000000

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int mylist[10000] = { 0, };

void merge(int mylist[], int left, int mid, int right) {
	int i = left, j = mid + 1, k = left;
	int sorted[10000] = { 0 }; // new array
	while (i <= mid && j <= right) {
		if (mylist[i] <= mylist[j]) {
			sorted[k++] = mylist[i++];
		}
		else {
			sorted[k++] = mylist[j++];
		}
	}

	while (i <= mid) {
		sorted[k++] = mylist[i++];
	}
	while (j <= right) {
		sorted[k++] = mylist[j++];
	}

	for (int a = left; a <= right; a++) {
		mylist[a] = sorted[a];
	}
}

void merge_sort(int list[], int left, int right) {
	if (left < right) {
		int mid = (left + right) / 2;
		merge_sort(list, left, mid);
		merge_sort(list, mid + 1, right);
		merge(list, left, mid, right);
	}
}

int binary_search(int mylist[], int left, int right) {
	int ret_value = 0;
	int init_left = left; int init_right = right;
	int target_value = -(mylist[left] + mylist[right]);
	int mid = 0;
	left += 1; right -= 1;
	while (left<=right)
	{
		mid = (left + right) / 2;
		if (mylist[mid] > target_value) {
			right = mid - 1;
		}
		else if (mylist[mid] < target_value) {
			left = mid + 1;
		}
		else {
			ret_value = 1;
			break;
		}
	}
	if (ret_value == 1) {
		int idx = mid;
		while (true)
		{
			idx += 1;
			if (idx == init_right || mylist[idx] != mylist[mid]) {
				break;
			}
			ret_value += 1;
		}
		idx = mid;
		while (true)
		{
			idx -= 1;
			if (idx == init_left || mylist[idx] != mylist[mid]) {
				break;
			}
			ret_value += 1;
		}
	}
	return ret_value;
}

int main() {
	int n;
	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		scanf("%d", &mylist[i]);
	}
	int answer = 0;
	merge_sort(mylist, 0, n-1);
	for (int left = 0; left < n - 2; left++) {
		for (int right = left + 2; right < n; right++) {
			answer += binary_search(mylist, left, right);
		}
	}
	printf("%d", answer);
	return 0;
}