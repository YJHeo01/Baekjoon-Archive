#include <stdio.h>
#include <stdlib.h>

int heap[100001] = { 0 };
int last_i = 0;
void heap_push(int x) {
	heap[++last_i] = x;
	int cur_i = last_i;
	int parent_i = last_i / 2;
	while (parent_i >= 1) {
		if (abs(heap[parent_i]) < abs(heap[cur_i])) {
			return;
		}
		if (abs(heap[parent_i]) == abs(heap[cur_i])) {
			if (heap[parent_i] <= heap[cur_i]) {
				return;
			}
		}
		int tmp = heap[parent_i];
		heap[parent_i] = heap[cur_i];
		heap[cur_i] = tmp;
		cur_i = parent_i;
		parent_i = parent_i / 2;
	}
}

int find_smallest(int a, int b) {
	if (heap[a] < heap[b]) {
		return a;
	}
	else {
		return b;
	}
}

int find_smallest_(int a, int b) {
	if (a <= last_i && abs(heap[b]) == abs(heap[a])) {
		if (heap[a] < heap[b]) {
			return a;
		}
	}
	return b;
}
int heap_pop() {
	if (last_i == 0) {
		return 0;
	}
	int ret_v = heap[1];
	heap[1] = heap[last_i--];
	int cur_i = 1;
	int left = 2* cur_i;
	int right = left + 1;
	int smallest = cur_i;
	while (1) {
		if (left <= last_i && abs(heap[smallest]) > abs(heap[left])) {
			smallest = left;
		}
		if (right <= last_i && abs(heap[smallest]) > abs(heap[right])) {
			smallest = right;
		}
		if (smallest == cur_i) {
			smallest = find_smallest_(left, smallest);
			smallest = find_smallest_(right, smallest);

			if (smallest == cur_i) {
				return ret_v;
			}
		}
		if (abs(heap[left]) == abs(heap[right])) {
			if (left <= last_i && right <= last_i)
			{
				smallest = find_smallest(left, right);
			}
		}

		int tmp = heap[smallest];
		heap[smallest] = heap[cur_i];
		heap[cur_i] = tmp;
		cur_i = smallest;
		left = 2 * cur_i;
		right = left + 1;
	}
	return ret_v;
}
int main() {
	int n,x,v;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &x);
		switch (x) {
		case 0:
			v = heap_pop();
			printf("%d\n", v);
			break;
		default:
			heap_push(x);
		}
		
	}
}