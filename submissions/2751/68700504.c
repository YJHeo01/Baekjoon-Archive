#include <stdio.h>
#include <stdlib.h>

int heap[1000001] = { 0 };
int last_i = 0;

void change_value(int a, int b) {
	int tmp = heap[a];
	heap[a] = heap[b];
	heap[b] = tmp;
}
void heap_push(int n) {
	heap[++last_i] = n;
	int cur = last_i;
	int parent = cur / 2;
	int tmp = 0;
	while (parent >= 1) {
		if (heap[parent] < heap[cur]) {
			return;
		}
		change_value(cur, parent);
		cur = parent;
		parent = parent / 2;
	}
}

int heap_pop(void) {
	int ret_v = heap[1];
	heap[1] = heap[last_i--];
	int cur = 1;
	int smallest = cur;
	int left = cur * 2;
	int right = left + 1;
	while (1) {
		if (heap[left] < heap[smallest] && left <= last_i) {
			smallest = left;
		}
		if (heap[right] < heap[smallest] && right <= last_i) {
			smallest = right;
		}
		if (smallest == cur) {
			return ret_v;
		}
		else {
			change_value(smallest, cur);
			cur = smallest;
			left = cur * 2;
			right = left + 1;
		}
	}
}
int main() {
	int n;
	scanf("%d", &n);
	int num = 0;
	for (int i = 0; i < n; i++)
	{
		scanf("%d", &num);
		heap_push(num);
	}
	for (int i = 0; i < n; i++) {
		printf("%d\n", heap_pop());
	}

}