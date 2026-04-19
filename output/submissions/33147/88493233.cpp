#include <iostream>

using namespace std;

int main() {

        ios::sync_with_stdio(false);

        cin.tie(NULL);

        int n, k;

        cin >> n >> k;

        for (int i = 0;i < n;i++) {

                int tmp;

                cin >> tmp;

                if (i % k != tmp % k) {

                        cout << "NO"; return 0;

                }

        }

        cout << "YES";

}