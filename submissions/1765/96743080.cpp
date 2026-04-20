#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int parent[1001] = { 0, };

int find_parent(int x) {
	if (parent[x] != x) {
		parent[x] = find_parent(parent[x]);
	}
	return parent[x];
}

void union_parent(int a, int b) {
	a = find_parent(a);
	b = find_parent(b);
	if (a < b) parent[b] = a;
	if (b < a) parent[a] = b;
}

int main(int argc, char** argv)
{
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(NULL);
	
	
	int n;

	cin >> n;
	
	for (int i = 1;i <= n;i++) parent[i] = i;

	vector<vector<int>> enemy(n + 1);

	int m;

	cin >> m;

	for (int i = 0;i < m;i++) {
		char c;
		int p, q;
		cin >> c >> p >> q; 
		if (c == 'E') {
			for (int x : enemy[p]) {
				union_parent(x, q);
			}
			for (int x : enemy[q]) {
				union_parent(x, p);
			}
			enemy[p].push_back(q);
			enemy[q].push_back(p);
		}
		else {
			union_parent(p, q);
		}
	}
	
	int answer = 0;

	for (int i = 1;i <= n;i++) {
		if (find_parent(i) == i) answer++;
	}

	cout << answer;

	return 0;
}