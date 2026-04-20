#include <stdio.h>

int find_parent(int parent[], int x) {
	if (parent[x] != x) {
		return find_parent(parent, parent[x]);
	}
}

int union_parent(int parent[], int a, int b) {
    int a_ = find_parent(parent, a);
        if (a_ == 1) {
            parent[b] = a;
        }
        else {
            parent[a] = b;
        }
}

int main()
{
    int n,i,a,b;
    int *parent[100001] = {0};
    scanf("%d", &n);
   
    for (i = 0; i < n + 1; i++) {
        parent[i] = i;
    }
    for (i = 0; i < n - 1; i++) {
        scanf("%d %d", &a, &b);
        union_parent(parent, a, b);
    }
    for (i = 2; i < n + 1; i++) {
        printf("%d\n", parent[i]);
    }
}