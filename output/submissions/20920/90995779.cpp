#include <iostream>
#include <unordered_map>
#include <algorithm>

using namespace std;

bool compare(pair<string, int> a, pair<string, int> b) {
	if (a.second != b.second) return a.second > b.second;
	if (a.first.size() != b.first.size()) return a.first.size() > b.first.size();
	return a.first < b.first;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
	int n, m;

	cin >> n >> m;

	unordered_map<string, int> table;

	for (int i = 0;i < n;i++) {
		string tmp;
		cin >> tmp;
		if (tmp.size() >= m) table[tmp]++;
	}

	vector<pair<string, int>> arr(table.begin(), table.end());

	sort(arr.begin(), arr.end(), compare);

	for (auto tmp : arr) cout << tmp.first << '\n';

}