#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
#include <map>

using namespace std;

char C[200001] = { 0, };

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL);
	
	int n;
	cin >> n;
	cin >> C;

	map<char, int> cnt;

	for (int i = 0;i < n / 2;i++) {
		cnt[C[i]] += 1;
		cnt[C[n - i - 1]] += 1;
	}

	bool possible = true;
	for (auto const &alphabet : cnt) {
		if (alphabet.second % 2 == 1) possible = false;
	}

	if (possible) cout << "Yes";
	else cout << "No";

}