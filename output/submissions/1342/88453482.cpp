#include <iostream>
#include <map>
#include <unordered_map>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL);
	
	string s;
	cin >> s;
	
	vector<int> data;
	for (int i = 0;i < s.length();i++) { data.push_back(i);}

	int answer = 0;
	unordered_map<string, int> exist;
	do {
		string tmp;
		for (int i : data) {
			tmp += s[i];
		}
		if (exist.find(tmp) != exist.end()) continue;
		exist.insert({ tmp,1 });
		answer += 1;
		for (int i = 1;i < s.length();i++) {
			if (tmp[i - 1] == tmp[i]) {
				answer -= 1;
				break;
			}
		}
	}
	while (next_permutation(data.begin(), data.end()));

	cout << answer;
}