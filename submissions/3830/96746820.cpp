#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int parent[100001] = { 0, };
int value[100001] = { 0, };

int find_parent(int x) {
	if (parent[x] == x) return x;
	int tmp;
	tmp = find_parent(parent[x]);
	value[x] += value[parent[x]];
	parent[x] = tmp;
	return parent[x];
}

void question(int x, int y) {
	int a = find_parent(x);
	int b = find_parent(y);
	if (a != b) cout << "UNKNOWN" << "\n";
	else cout << value[y] - value[x] << "\n";
}

int main(int argc, char** argv)
{
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(NULL);
	
	while (1) {
		int n, m;
		cin >> n >> m;
		if (n == 0 and m == 0) break;
		for (int i = 1;i <= n;i++) {
			parent[i] = i;
			value[i] = 0;
		}
		for (int i = 0;i < m;i++) {
			char command;
			int a, b;
			cin >> command >> a >> b;
			if (command == '!') {
				int w;
				cin >> w;
				int root_a = find_parent(a);
				int root_b = find_parent(b);
				if (root_a == root_b) continue;
				parent[root_a] = root_b;
				value[root_a] = value[b] - value[a] - w;
			}
			else {
				question(a, b);
			}
		}
	}

	return 0;
}