#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

vector<vector<char>> a;
vector<vector<int>> s;

int cnt[100001] = { 0, };

int binary_search(vector<int>& arr, int target) {
	int right = arr.size() - 1;
	int left = 0;
	while (left <= right) {
		int mid = (left + right) / 2;
		if (target > arr[mid]) left = mid + 1;
		else if (target < arr[mid])right = mid - 1;
		else return mid;
	}
	return 0;
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

int query(vector<int>& s, vector<char>& a, int node, int target, int start, int end) {
	if (start == end) return end;
	int mid = (start+end) / 2;
	if (s[node * 2] >= target) return query(s, a, node * 2, target, start, mid);
	else return query(s, a, node * 2 + 1, target - s[node * 2], mid + 1, end);
}

void dfs(vector<vector<int>>& graph, vector<bool>& visited, int x) {
	if (visited[x] == false) {
		cout << x << " ";
		visited[x] = true;
		int tree_size = s[x].size() / 2;
		for (int i = 0;i < graph[x].size();i++) {
			if (a[x][i] != 0) update(s[x], tree_size + i, 1);
		}
		//노드 x를 방문하면, 노드 x와 인접한 노드에서 x를 방문할 수 없으므로, 인접한 노드의 방문 가능한 노드 수를 줄인다
		for (int nx : graph[x]) {
			cnt[nx] -= 1;
			int idx = binary_search(graph[nx], x);
			a[nx][idx] = 0;
			update(s[nx], idx + s[nx].size() / 2, 0);
		}
	}

	while (1) {
		if (cnt[x] == 0) break;
		int target = 1;
		if (cnt[x] % 2 == 1) target += (cnt[x] / 2);
		int nx = graph[x][query(s[x], a[x], 1, target, 0, graph[x].size()-1)];
		dfs(graph, visited, nx);
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
		graph[a].push_back(b);
		graph[b].push_back(a);
	}

	for (int i = 0;i <= N;i++) {
		sort(graph[i].begin(), graph[i].end());
		cnt[i] = graph[i].size();
	}

	for (int i = 0;i <= N;i++) {
		vector<char> tmp(graph[i].size(), 1);
		int tree_size = 1 << max(1,(int)ceil(max(1.0,log2(graph[i].size()))));
		vector<int> tree(tree_size * 2, 0);
		s.push_back(tree);
		a.push_back(tmp);
	}

	vector<bool> visited(N + 1, false);

	dfs(graph, visited, 1);

	return 0;
}