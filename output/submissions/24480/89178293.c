#include <stdio.h>
#include <stdlib.h>


int edge[200000][2] = { 0, };
int edge_cnt[100001] = { 0, };
int visited[100001] = { 0, };
int visit_num = 1;
int* adj_list[100001] = { 0, };
int adj_list_idx[100001] = { 0, };
void dfs(int vx);
int compare(const int *a, const int *b);

int main() {
	int n, m, r;
	
	scanf("%d %d %d", &n, &m, &r);
	
	for (int i = 0;i < m;i++) {
		int u, v;
		scanf("%d %d", &u, &v);
		edge_cnt[u]++; edge_cnt[v]++;
		edge[i][0] = u;edge[i][1] = v;
	}

	for (int i = 1;i <= n;i++) {
		adj_list[i] = (int*)malloc(sizeof(int) * edge_cnt[i]);
	}

	for (int i = 0;i < m;i++) {
		int u = edge[i][0];
		int v = edge[i][1];
		*(adj_list[u] + adj_list_idx[u]++) = v;
		*(adj_list[v] + adj_list_idx[v]++) = u;
	}
	
	for (int i = 1;i <= n;i++) {
		if (edge_cnt[i] == 0 || adj_list[i] == 0) continue;
		qsort(adj_list[i], edge_cnt[i], sizeof(int), compare);
	}
	
	visited[r] = 1;
	dfs(r);

	for (int i = 1;i <= n;i++) {
		printf("%d\n", visited[i]);
	}
}

int compare(const int* a, const int* b) {
	return(*b - *a);
}


void dfs(int vx) {
	for (int i = 0;i < edge_cnt[vx];i++) {
		int nx = *(adj_list[vx] + i);
		if (visited[nx] != 0) continue;
		visited[nx] = ++visit_num;
		dfs(nx);
	}
}