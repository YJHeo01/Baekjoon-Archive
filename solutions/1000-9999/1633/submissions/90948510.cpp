#include <iostream>
#include <queue>
#include <vector>

using namespace std;


int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	priority_queue<vector<int>> pq;
	int black = 15;
	int white = 15;
	int idx = 0;
	
	while (1) {
		int a, b;
		cin >> a >> b;
		if (cin.eof()==true) break;
		pq.push({ a,a - b,0,idx });
		pq.push({ b,b - a,1,idx });
		idx += 1;
	}
	
	vector<bool> use(pq.size(), false);
	int answer = 0;
	
	while (white != 0 or black != 0) {
		vector<int> tmp = pq.top();
		pq.pop();
		if (use[tmp[3]]) continue;
		if (tmp[2] == 0) {
			if (white == 0) continue;
			white--;
		}
		else {
			if (black == 0) continue;
			black--;
		}
		answer += tmp[0];
		use[tmp[3]] = true;
	}
	cout << answer;

}