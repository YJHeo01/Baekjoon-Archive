#include <stdio.h>

int n;
int array_A[4000] = { 0, };
int array_B[4000] = { 0, };
int array_C[4000] = { 0, };
int array_D[4000] = { 0, };

void merge(int mylist[], int left, int mid, int right) {
	int i = left, j = mid + 1, k = left;
	int sorted[4000] = { 0 }; // new array
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

int binary_search(int _array[], int target) {
	int left = 0;
	int right = n - 1;
	while (left<=right)
	{
		int mid = (left + right) / 2;
		if (_array[mid] < target) {
			left = mid + 1;
		}
		else if (_array[mid] > target) {
			right = mid - 1;
		}
		else {
			return 1;
		}
	}
	return 0;
}

int main() {

	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d %d %d %d", &array_A[i], &array_B[i], &array_C[i], &array_D[i]);
	}
	int answer = 0;
	merge_sort(array_D, 0, n - 1);
	for (int A_idx = 0; A_idx < n; A_idx++) {
		for (int B_idx = 0; B_idx < n; B_idx++) {
			for (int C_idx = 0; C_idx < n; C_idx++) {
				int value = array_A[A_idx] + array_B[B_idx] + array_C[C_idx];
				if (value + array_D[0] > 0 || value + array_D[n - 1] < 0) {
					continue;
				}
				answer += binary_search(array_D, -value);
			}
		}
	}
	printf("%d", answer);
}