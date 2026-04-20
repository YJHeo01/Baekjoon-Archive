#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>



typedef struct _SLL {
	int node;
	struct _SLL* next;
}SLL;

SLL* node_head[100001] = { 0, };
SLL* node_last[100001] = { 0, };
SLL* adj_list_head[100001] = { 0, };
SLL* adj_list_last[100001] = { 0, };

int visited[100001] = { 0, };
int visit_num = 1;


void insert(int vx, int nx) {
	SLL* new_node = (SLL*)malloc(sizeof(SLL));
	new_node->node = nx;
	new_node->next = 0;
	if (node_head[vx] == 0) {
		node_head[vx] = new_node;
		node_last[vx] = new_node;
	}
	else {
		node_last[vx]->next = new_node;
		node_last[vx] = node_last[vx]->next;
	}
}

void adj_graph(int vx) {
	SLL* tmp = node_head[vx];
	while (1) {
		if (tmp == 0) break;
		int nx = tmp->node;
		SLL* new_node = (SLL*)malloc(sizeof(SLL));
		new_node->node = vx;
		new_node->next = 0;
		if (adj_list_head[nx] == 0) {
			adj_list_head[nx] = new_node;
			adj_list_last[nx] = new_node;
		}
		else {
			adj_list_last[nx]->next = new_node;
			adj_list_last[nx] = adj_list_last[nx]->next;
		}
		tmp = tmp->next;
	}
}



void dfs(int vx) {
	SLL* tmp = adj_list_head[vx];
	while (1) {
		if (tmp == 0) break;
		int nx = tmp->node;
		if (visited[nx] == 0) {
			visit_num += 1;
			visited[nx] = visit_num;
			dfs(nx);
		}
		tmp = tmp->next;
	}
}
int main() {
	int n, m, r;
	
	scanf("%d %d %d", &n, &m, &r);

	for (int i = 1;i <= n;i++) {
		node_head[i] = 0;
		node_last[i] = 0;
	}
	
	for (int i = 0;i < m;i++) {
		int u, v;
		scanf("%d %d", &u, &v);
		insert(u, v);
		insert(v, u);
	}

	for (int i = 1;i <= n;i++) {
		adj_graph(i);
	}

	visited[r] = 1;
	dfs(r);

	for (int i = 1;i <= n;i++) {
		printf("%d\n", visited[i]);
	}
}