#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>

using namespace std;

vector<vector<int>> a;
vector<vector<int>> s;

int cnt[100001] = { 0, };
string answer;

int binary_search(vector<int>& arr, int target) {
	int right = arr.size() - 1;
	int left = 0;
	while (left <= right) {
		int mid = (left + right) / 2;
		if (target > arr[mid]) left = mid + 1;
		else if (target < arr[mid])right = mid - 1;
		else return mid;
	}
}

// 세그먼트 트리
void update(vector<int>&s, int node, int value) {
	s[node] = value;
	node /= 2;
	while (node) {
		s[node] = s[node * 2] + s[node * 2 + 1];
		node /= 2;
	}
}

int query(vector<int>&s, int left, int right) {
	int ret_value = 0;
	while (left <= right) {
		if (left % 2 == 1) {
			ret_value += s[left];
			left += 1;
		}
		if (right % 2 == 0) {
			ret_value += s[right];
			right -= 1;
		}
		left /= 2;right /= 2;
	}
	return ret_value;
}
void dfs(vector<vector<int>>& graph, vector<bool>& visited, int x) {
	if (visited[x] == false) {
		answer += to_string(x);
		answer += ' ';
		visited[x] = true;
		int tree_size = s[x].size() / 2;
		for (int i = 0;i < graph[x].size();i++) {
			if(a[x][i]!=0) update(s[x], tree_size + i, 1);
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

		int tree_size = s[x].size() / 2;

		int target = 1;
		if (cnt[x] % 2 == 1) target += (cnt[x] / 2);

		int nx = graph[x].back();
		int left = 0;
		int right = graph[x].size() - 1;
		while (left <= right) {
			int mid = (left + right) / 2;
			int tmp = query(s[x], tree_size, mid + tree_size);
			if (tmp > target) right = mid - 1;
			else if (tmp < target) left = mid + 1;
			else {
				if (visited[graph[x][mid]]) right = mid - 1;
				else { nx = graph[x][mid];break; }
			}
		}
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
		vector<int> tmp(graph[i].size(),1);
		int tree_size = 1 << (int)ceil(log2(graph[i].size()));
		vector<int> tree(tree_size * 2, 0);
		s.push_back(tree);
		a.push_back(tmp);
	}

	vector<bool> visited(N + 1, false);

	dfs(graph, visited, 1);

    cout << answer;
	return 0;
}