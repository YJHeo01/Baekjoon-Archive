//https://www.acmicpc.net/source/91002691 gpt로 변환

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    // n/2 (정수 나눗셈) : 왼쪽 절반 길이
    int half_len = n / 2;
    // 생성해야 할 “자유 자리”의 수: ceil(half_len/2) == (n/4) + ((n/2) % 2)
    int free_digits = (n / 4) + ((n / 2) % 2);
    
    // pelin: 왼쪽 절반(회문 형태)의 문자열을 저장하는 벡터
    vector<string> pelin;

    // 자유 자리 조합의 총 개수: 10^free_digits
    int total = 1;
    for (int i = 0; i < free_digits; i++) {
        total *= 10;
    }
    
    // 0부터 total-1까지를 문자열로 변환(자유 자리 숫자, 자릿수 부족 시 앞에 0을 채움)
    // 이후 이를 이용하여 회문 형태의 왼쪽 절반 문자열을 구성
    for (int num = 0; num < total; num++) {
        string free_str = "";
        int temp = num;
        // free_digits 자리 숫자 생성 (역순으로 얻어지므로)
        for (int i = 0; i < free_digits; i++) {
            free_str.push_back('0' + (temp % 10));
            temp /= 10;
        }
        // 올바른 순서를 위해 뒤집음
        reverse(free_str.begin(), free_str.end());
        
        // 왼쪽 절반의 길이는 half_len.
        // 회문 특성: 각 자리 i에 대해, free_str[min(i, half_len - i - 1)] 를 사용
        string pal = "";
        for (int i = 0; i < half_len; i++) {
            int idx = i < (half_len - i - 1) ? i : (half_len - i - 1);
            pal.push_back(free_str[idx]);
        }
        pelin.push_back(pal);
    }
    
    // l = total (자유 자리 조합의 수)
    // 각 pelin[i]는 half_len 자리 문자열임
    // 완전한 숫자는 pelin[i] + pelin[j] 의 연결로 만들어지며, 이는 n자리 수가 됨
    // 하지만 직접 큰 수로 변환하면 오버플로우 위험이 있으므로 모듈러 연산을 이용
    // (A * 10^(half_len) + B) % m == 0 인지 검사
    
    // 10^(half_len) mod m 미리 계산
    long long modPow = 1;
    for (int i = 0; i < half_len; i++){
        modPow = (modPow * 10LL) % m;
    }
    
    // 각 pelin 문자열에 대해, 정수값 mod m 를 계산하여 저장
    vector<long long> mods;
    for (auto &s : pelin) {
        long long val = 0;
        for (char c : s) {
            val = (val * 10 + (c - '0')) % m;
        }
        mods.push_back(val);
    }
    
    long long answer = 0;
    int size = pelin.size();
    for (int i = 0; i < size; i++){
        // pelin[i]가 '0'으로 시작하면 n자리 수의 맨 앞자리가 0이 되므로 건너뜀
        if (pelin[i][0] == '0') continue;
        for (int j = 0; j < size; j++){
            // 전체 수 mod m = (mods[i] * 10^(half_len) + mods[j]) % m
            long long fullMod = (mods[i] * modPow + mods[j]) % m;
            if (fullMod == 0) {
                answer++;
            }
        }
    }
    
    cout << answer << "\n";
    return 0;
}
