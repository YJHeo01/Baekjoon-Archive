#include <iostream>
#include <map>
#include <set>
#include <unordered_map>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL);

	string s;
	cin >> s;

	vector<int> data;
	for (int i = 0;i < s.length();i++) { data.push_back(i); }

	set<string> mySet;
	do {
		string tmp;
		for (int i : data) {
			tmp += s[i];
		}
		bool lucky = true;
		for (int i = 1;i < s.length();i++) {
			if (tmp[i - 1] == tmp[i]) {
				lucky = false;
				break;
			}
		}
		if (lucky) {
			mySet.insert(tmp);
		}
	} while (next_permutation(data.begin(), data.end()));

	cout << mySet.size();
}