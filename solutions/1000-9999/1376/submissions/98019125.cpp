#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

vector<int> s[100001];

int binary_search(vector<int>& arr, int target) {
	int right = arr.size() - 1;
	int left = 0;
	while (left <= right) {
		int mid = (left + right) / 2;
		if (target > arr[mid]) left = mid + 1;
		else right = mid - 1;
	}
	return left;
}

// 세그먼트 트리
void update(vector<int>& s, int node, int value) {
	s[node] = value;
	node /= 2;
	while (node) {
		s[node] = s[node * 2] + s[node * 2 + 1];
		node /= 2;
	}
}

int query(vector<int>& s, int node, int target, int start, int end) {
	if (start == end) return end;
	int mid = (start + end) / 2;
	if (s[node * 2] > target) return query(s, node * 2, target, start, mid);
	else return query(s, node * 2 + 1, target - s[node * 2], mid + 1, end);
}

void dfs(vector<vector<int>>& graph, int x) {


	cout << x << " ";
	for (int nx : graph[x]) {
		int idx = binary_search(graph[nx], x);
		update(s[nx], s[nx].size() / 2 + idx, 0);
	}

	while (s[x][1]) {
		int tree_size = s[x].size() / 2;
		//노드 x를 방문하면, 노드 x와 인접한 노드에서 x를 방문할 수 없으므로, 인접한 노드의 방문 가능한 노드 수를 줄인다


		int target = 0;
		if (s[x][1] % 2 != 0) {
			target = s[x][1] / 2;
		}

		//cout << target << "\n";
		int nx = graph[x][query(s[x], 1, target, 0, s[x].size() / 2 - 1)];
		if (nx == x) return;
		dfs(graph, nx);
	}
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(NULL);

	int N, M;

	cin >> N >> M;

	vector<vector<int>> graph(N + 1);

	for (int i = 0;i < M;i++) {
		int a, b;
		cin >> a >> b;
		if (a == b) continue;
		graph[a].push_back(b);
		graph[b].push_back(a);
	}

	for (int i = 0;i <= N;i++) {
		sort(graph[i].begin(), graph[i].end());
		graph[i].erase(unique(graph[i].begin(), graph[i].end()), graph[i].end());
		sort(graph[i].begin(), graph[i].end());
	}

	for (int i = 0;i <= N;i++) {
		int tree_size = 1 << max(1, (int)ceil(max(1.0, log2(graph[i].size()))));
		vector<int> tree(tree_size * 2, 0);
		for (int j = 0;j < graph[i].size();j++)update(tree, j + tree_size, 1);
		s[i] = tree;
	}


	for (int i = 0;i <= N;i++) {
		//cout << s[i][1] << "\n";
	}
	dfs(graph, 1);

	return 0;
}