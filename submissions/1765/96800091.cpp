#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int parent[1001] = { 0, };
bool visited[1001] = { false, };

void dfs(vector<vector<int>>& graph, int x) {
	for (int nx : graph[x]) {
		if (visited[nx]) continue;
		visited[nx] = true;
		dfs(graph, nx);
	}
}

int main(int argc, char** argv)
{
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(NULL);


	int n;

	cin >> n;

	for (int i = 1;i <= n;i++) parent[i] = i;

	vector<vector<int>> enemy(n + 1);

	vector<vector<int>> graph(n + 1);

	int m;

	cin >> m;

	for (int i = 0;i < m;i++) {
		char c;
		int p, q;
		cin >> c >> p >> q;
		if (c == 'E') {
			for (int x : enemy[p]) {
				graph[x].push_back(p);
				graph[p].push_back(x);
			}
			for (int x : enemy[q]) {
				graph[x].push_back(q);
				graph[q].push_back(x);
			}
			enemy[p].push_back(q);
			enemy[q].push_back(p);
		}
		else {
			graph[p].push_back(q);
			graph[q].push_back(p);
		}
	}

	int answer = 0;


	for (int i = 1;i <= n;i++) {
		visited[i] = false;
	}

	for (int i = 1;i <= n;i++) {
		if (visited[i]) continue;
		answer++;
		visited[i] = true;
		dfs(graph, i);
	}
	cout << answer;

	return 0;
}