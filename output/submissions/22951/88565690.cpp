#include <iostream>

using namespace std;

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL);

	int n, k;
	cin >> n >> k;
	
	bool visited[1000] = { 0, };
	int card_value[1000];
	int card_cnt = n * k;
	
	for (int i = 0;i < card_cnt;i++) {
		int tmp;
		cin >> tmp;
		card_value[i] = tmp;
	}

	int idx = 0;
	int distance = 0;
	
	for (int i = 0;i < card_cnt;i++) {
		while (distance) {
			idx += 1; idx %= card_cnt;
			if (visited[idx] == false) distance -= 1;
		}
		
		visited[idx] = true;
		distance = card_value[idx];
	}

	int winner_id = idx / k + 1;
	cout << winner_id << " " << distance;

	return 0;
}