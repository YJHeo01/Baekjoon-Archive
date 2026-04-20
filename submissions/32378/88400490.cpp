#include <iostream>

using namespace std;

long long int grow[200000] = {};
long long int dp[200001][37] = {};

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL);
	
	int n, k, s;
	cin >> n >> k >> s;
	
	if (k > 36) { cout << "MEGA";return 0; }
	
	for (int i = 0;i < n;i++) { cin >> grow[i];}
	
	dp[0][0] = s;
	for (int day = 0;day < n;day++) {
		for (int power_up = 0;power_up < k;power_up++) {
			if (dp[day][power_up] <= 0) continue;
			dp[day + 1][power_up] = max(dp[day + 1][power_up], dp[day][power_up] + grow[day]);
			dp[day + 1][power_up + 1] = max(dp[day + 1][power_up + 1], dp[day][power_up] * 2);
		}
		if (dp[day][k] > 0) dp[day + 1][k] = max(dp[day + 1][k], dp[day][k] + grow[day]);
	}
	
	long long int answer = 0;
	for (auto i : dp[n]) {
		answer = max(answer, i);
	}

	if (answer <= 0) cout << -1;
	else if (answer > 100000000000) cout << "MEGA";
	else cout << answer;
}