#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	vector<vector<int>> arr;

	while (1) {
		int a, b;
		cin >> a >> b;
		if (cin.eof()==true) break;
		arr.push_back({a,b});
	}

	vector<vector<vector<int>>> dp(arr.size() + 1, vector<vector<int>>(16, vector<int>(16, 0)));
	
	for (int i = 0;i < arr.size();i++) {
		for (int white = 0;white < 15;white++) {
			for (int black = 0;black < 15;black++) {
				dp[i + 1][white + 1][black] = max(dp[i][white + 1][black], dp[i][white][black] + arr[i][1]);
				dp[i + 1][white][black + 1] = max(dp[i][white][black + 1], dp[i][white][black] + arr[i][0]);
			}
		}
	}

	cout << dp[arr.size()][15][15];
}