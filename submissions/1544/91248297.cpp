#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;

    cin >> n;

    vector<string> word_list;

    for (int i = 0;i < n;i++) {
        string tmp;
        cin >> tmp;
        word_list.push_back(tmp);
    }

    vector<bool> remove(n, false);

    for (int i = 0;i < n;i++) {
        if (remove[i]) continue;
        for (int j = 0;j < i;j++) {
            if (remove[j] or word_list[i].size() != word_list[j].size()) continue;
            for (int k = 0;k < word_list[i].size();k++) {
                bool target = true;
                for (int x = 0;x < word_list[i].size();x++) {
                    if (word_list[i][x] != word_list[j][(x + k)% word_list[i].size()]) target = false;
                }
                if (target) remove[j] = true;
            }
            
        }
    }

    int answer = 0;

    for (int i = 0;i < n;i++) {
        if (remove[i] == false) answer++;
    }

    cout << answer;
}