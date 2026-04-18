#include <iostream>

#define INF 987654321

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int n, m, k;

	cin >> n >> m >> k;

	int adj_matrix[20][20] = { 0, };

	for (int i = 0;i < n;i++) {
		fill(adj_matrix[i], adj_matrix[i + 1], INF);
		adj_matrix[i][i] = 0;
	}

	for (int i = 0;i < m;i++) {
		int a, b, c;
		cin >> a >> b >> c;
		a--;b--;
		adj_matrix[a][b] = min(adj_matrix[a][b], c);
		adj_matrix[b][a] = min(adj_matrix[b][a], c);
	}

	for (int x = 1;x < n;x++) {
		for (int i = 0;i < n;i++) {
			for (int j = 0;j < n;j++) {
				adj_matrix[i][j] = min(adj_matrix[i][j], adj_matrix[i][x] + adj_matrix[x][j]);
			}
		}
	}

	int bit_mask = 1;
	int tsp[1 << 19][19] = { 0, };

	for (int i = 0;i < (1 << (n - 1));i++) {
		for (int j = 0;j < (n - 1);j++) {
			tsp[i][j] = INF;
		}
	}

	for (int i = 1;i < n;i++) {
		tsp[bit_mask][i - 1] = adj_matrix[0][i];
		bit_mask <<= 1;
	}

	int need_hp[20] = { 0, };
	fill(need_hp, need_hp + 20, INF);

	for (int bit = 1;bit < 1 << (n - 1);bit++) {
		int cnt = __builtin_popcount(bit);
		for (int x = 1;x < n;x++) {
			int i = x - 1;
			if (tsp[bit][i] == INF) continue;
			need_hp[cnt] = min(need_hp[cnt], tsp[bit][i] + adj_matrix[x][0]);
			for (int nx = 1;nx < n;nx++) {
				int j = nx - 1;
				int next_bit = bit | (1 << j);
				if (adj_matrix[x][nx] == INF or next_bit == bit) continue;
				tsp[next_bit][j] = min(tsp[next_bit][j], tsp[bit][i] + adj_matrix[x][nx]);
			}
		}
	}

	int knapsack[100001] = { 0, };

	int answer = 0;
	for (int hp = 0;hp <= k;hp++) {
		answer = max(answer, knapsack[hp]);
		for (int cnt = 1;cnt < n;cnt++) {
			if (hp + need_hp[cnt] > k) continue;
			knapsack[hp + need_hp[cnt]] = max(knapsack[hp] + cnt * cnt, knapsack[hp + need_hp[cnt]]);
		}
	}

	cout << answer;

	return 0;
}